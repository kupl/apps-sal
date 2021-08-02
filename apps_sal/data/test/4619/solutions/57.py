w, h, n = map(int, input().split())
a = [[int(i)for i in input().split()]for j in range(n)]
S = [[0, w], [0, h]]
for i in a:
    if i[2] == 1:
        S[0][0] = max(i[0], S[0][0])

    if i[2] == 2:
        S[0][1] = min(i[0], S[0][1])

    if i[2] == 3:
        S[1][0] = max(i[1], S[1][0])

    if i[2] == 4:
        S[1][1] = min(i[1], S[1][1])

ans = max(0, (S[0][1] - S[0][0])) * max(0, (S[1][1] - S[1][0]))
print(ans)
