

from fractions import gcd
P = 10**9 + 7
N = int(input())
S = list(map(int, input().split()))

temp = S[0]
for i in range(1, N):
    temp = temp * S[i] // gcd(temp, S[i])
temp %= P

ans = 0
for num in S:
    ans = ((temp * pow(num, P - 2, P)) % P + ans) % P
print(ans)
