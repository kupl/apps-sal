n, w, v, u = list(map(int, input().split()))
ans = 0
flag1 = 0
flag2 = 0

for i in range(n):
    x, y = list(map(int, input().split()))
    if x/v < y/u:
        flag1 = 1
    if x/v > y/u:
        flag2 = 1
    ans = max(ans, x/v+(w-y)/u)

if flag1+flag2 == 2:
    print(ans)
else:
    print(w/u)

