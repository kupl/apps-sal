N = int(input())
S = list(input())

r = S.count('R')
g = S.count('G')
b = S.count('B')

ans = r * g * b
for j in range(1, N):
    t = 1
    while j - t >= 0 and j + t <= N - 1:
        if S[j - t] != S[j] and S[j] != S[j + t] and S[j + t] != S[j - t]:
            ans -= 1
        t += 1

print(ans)
return
