from collections import Counter as co
n = int(input())
c = co(map(int, input().split()))
ans = pow(2, n // 2, 10**9 + 7)
if n % 2:
    if 0 not in c or c[0] > 1:
        ans = 0
    for i in range(1, n):
        if i % 2 == 0:
            if i not in c or c[i] != 2:
                ans = 0
                break
        else:
            if i in c:
                ans = 0
                break
else:
    if 0 in c:
        ans = 0
    for i in range(1, n):
        if i % 2:
            if i not in c or c[i] != 2:
                ans = 0
                break
        else:
            if i in c:
                ans = 0
                break
print(ans)
