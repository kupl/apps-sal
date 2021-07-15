from math import gcd
n = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += a-1
print(ans)
