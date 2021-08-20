import sys
sys.setrecursionlimit(10 ** 6)
(n, a, b) = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    if tmp >= a and tmp <= b:
        ans += i
print(ans)
