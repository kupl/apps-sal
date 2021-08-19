N = int(input())
S = input()
uns = 0
for d in range(1, (N - 1) // 2 + 1):
    for i in range(N - 2 * d):
        (s, t, u) = (S[i], S[i + d], S[i + 2 * d])
        if s != t and t != u and (u != s):
            uns += 1
r = S.count('R')
g = S.count('G')
b = N - r - g
ans = r * g * b - uns
print(ans)
