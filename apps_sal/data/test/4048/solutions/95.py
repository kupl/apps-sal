import sys
n = int(input())

ans = float("inf")
flag = 0
for i in range(2, int(n**(1 / 2)) + 1):
    if n % i == 0:
        ans = min(ans, i + (n // i) - 2)
        flag = 1

if flag:
    print(ans)
else:
    print(n - 1)
