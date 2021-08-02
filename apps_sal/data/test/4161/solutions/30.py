import math

N = int(input())
ans = 0
for i in range(1, N + 1):
    for j in range(i, N + 1):
        for k in range(j, N + 1):
            if i == j and j == k:
                ans += i
            elif i < j and j < k:
                ans += 6 * math.gcd(i, math.gcd(j, k))
            else:
                ans += 3 * math.gcd(i, math.gcd(j, k))
print(ans)
