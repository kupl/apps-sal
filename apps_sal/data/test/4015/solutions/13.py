n,m = list(map(int,input().split()))
num = m / n
flag = 1
ans = 0
while num > 1:
    if num % 2 == 0:
        num //= 2
        ans += 1
        continue
    if num % 3 == 0:
        num //= 3
        ans += 1
        continue
    flag = 0
    break
if flag:
    print(ans)
else:
    print(-1)

