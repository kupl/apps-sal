(N, S) = list(map(str, input().split()))
N = int(N)
ans = 0
for i in range(N):
    c1 = 0
    c2 = 0
    for j in range(i, N):
        if S[j] == 'A':
            c1 += 1
        elif S[j] == 'T':
            c1 -= 1
        elif S[j] == 'G':
            c2 += 1
        else:
            c2 -= 1
        if c1 == 0 and c2 == 0:
            ans += 1
print(ans)
