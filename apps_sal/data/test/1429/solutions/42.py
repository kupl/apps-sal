N, S = map(str, input().split())
N = int(N)

ans = 0
for i in range(N):
    a = 0
    t = 0
    c = 0
    g = 0
    for j in range(i, N):
        if S[j] == "A":
            a += 1
        elif S[j] == "T":
            t += 1
        elif S[j] == "C":
            c += 1
        else:
            g += 1

        if a == t and c == g:
            ans += 1

print(ans)
