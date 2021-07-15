import math

n = int(input())
al = list(map(int, input().split()))

ans = math.gcd(al[0], al[1])

for i in range(2, n):
    ans = math.gcd(ans, al[i])

print(ans)
