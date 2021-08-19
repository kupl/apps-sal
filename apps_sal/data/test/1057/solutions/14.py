n = int(input())
S = input()
n = 0
m = 0
p = 998244353
for s in S:
    if s != S[0]:
        break
    n += 1
for s in S[::-1]:
    if s != S[-1]:
        break
    m += 1
ans = (n + 1) * (m + 1) if S[0] == S[-1] else n + m + 1
print(ans % 998244353)
