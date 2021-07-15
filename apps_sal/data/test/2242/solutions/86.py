S = input()
mod = 2019

t = len(S)
l = [0] * (t + 1)
for i in range(t-1, -1, -1):
    l[i] = (l[i+1] + int(S[i]) * pow(10, t-i-1, mod)) % mod

from collections import Counter

def nC2(n):
    return n * (n - 1) // 2

l = list(Counter(l).values())

ans = 0
for i in l:
    ans += nC2(i)

print(ans)
