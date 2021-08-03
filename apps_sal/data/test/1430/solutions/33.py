N, K = map(int, input().split())
S = input() + "2"
L = []
cnt = 0
temp = int(S[0])

for x in S:
    if temp == int(x):
        cnt += 1
    else:
        L.append(cnt)
        cnt = 1
        temp = int(x)

if S[0] == "0":
    Lcs = [0, 0]
else:
    Lcs = [0]

for x in L:
    Lcs.append(Lcs[-1] + x)

ans = Lcs[1]
N = len(Lcs)
i = 2

if i + 2 * (K - 1) > N - 1:
    print(Lcs[-1])
else:
    while i + 2 * (K - 1) <= N - 1:
        if i + 2 * (K - 1) == N - 1:
            ans = max(ans, Lcs[i + 2 * (K - 1)] - Lcs[i - 2])
        else:
            ans = max(ans, Lcs[i + 2 * (K - 1) + 1] - Lcs[i - 2])
        i += 2
    print(ans)
