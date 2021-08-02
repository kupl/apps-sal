from math import sqrt
p, y = map(int, input().split())
ans = y
while ans != 1:
    find = True
    if ans <= p:
        ans = 1
        continue
    for i in range(2, min(p + 1, int(sqrt(ans)) + 1)):
        if ans % i == 0:
            find = False
            break
    if find:
        break
    ans -= 1
if ans == 1:
    print(-1)
else:
    print(ans)
