n,m = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)

sum = 0
cnt = 0
for i in li:
    sum += i
    
for i in range(m):
    if li[m-1]*4*m >= sum:
        cnt += 1

if cnt == m:
    print('Yes')
else:
    print('No')
