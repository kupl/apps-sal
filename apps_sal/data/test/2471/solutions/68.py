def add_memo(tate,yoko):
    nonlocal memo
    if 2 <= tate <= h-1:
        if 2 <= yoko <= w-1:
            memo.append([tate,yoko])

h,w,n = list(map(int,input().split()))
#print(s)
memo = []
for i in range(0,n):
    x,y = list(map(int,input().split()))
    add_memo(x-1,y-1)
    add_memo(x-1,y)
    add_memo(x-1,y+1)
    add_memo(x,y-1)
    add_memo(x,y)
    add_memo(x,y+1)
    add_memo(x+1,y-1)
    add_memo(x+1,y)
    add_memo(x+1,y+1)

memo.sort()
ans = [0] * 10
ans[0] = (h-2)*(w-2)
tmp_x = 0
tmp_y = 0
count = 0
for i in range(0,len(memo)):
    if tmp_x == memo[i][0] and tmp_y == memo[i][1]:
        ans[count] -= 1
        count += 1
        ans[count] += 1
    else:
        ans[0] -= 1
        count = 1
        ans[count] += 1
    tmp_x = memo[i][0]
    tmp_y = memo[i][1]
#    print(memo[i],count)

for i in range(0,10):
    print((ans[i]))

