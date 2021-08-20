n = int(input())
A = list(map(int, input().split()))
S = [0]
cnt = 0
for i in range(n):
    cnt += A[i]
    S.append(cnt)
ans = S[n]
d1 = 1
d3 = 2
for d2 in range(2, n - 1):
    L = S[d2]
    R = S[n] - S[d2]
    for i in range(d1, d2):
        if S[i] >= L / 2:
            break
    if abs(S[i] - L / 2) >= abs(S[i - 1] - L / 2):
        d1 = i - 1
    else:
        d1 = i
    for i in range(d3, n):
        if S[i] - S[d2] >= R / 2:
            break
    if abs(S[i] - S[d2] - R / 2) >= abs(S[i - 1] - S[d2] - R / 2):
        d3 = i - 1
    else:
        d3 = i
    s = [S[d1], S[d2] - S[d1], S[d3] - S[d2], S[n] - S[d3]]
    ans = min(max(s) - min(s), ans)
print(ans)
