N = int(input())
S = input()
a = [0]
for i in range(N):
    a.append(a[-1])
    if S[i] == 'W':
        a[-1] += 1
ans = N
for i in range(N):
    ans = min(ans, a[i] + N - (i + 1) - (a[N] - a[i + 1]))
print(ans)
