N = int(input())
S = list(input())
r, g, b = 0, 0, 0
for s in S:
    if s == 'R':
        r += 1
    elif s == 'G':
        g += 1
    else:
        b += 1
ans = r * g * b
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = 2 * j - i
        if k < N:
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
print(ans)
