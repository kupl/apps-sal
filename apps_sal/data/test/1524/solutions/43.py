def RunLengthEncoding(S):
    res = []
    N = len(S)
    i = 0
    while i < N:
        cnt = 1
        while i < N - 1 and S[i] == S[i + 1]:
            cnt += 1
            i += 1
        res.append((S[i], cnt))
        i += 1
    return res


S = input()
N = len(S)
rle = RunLengthEncoding(S)

goal = []
for i, (l, r) in enumerate(zip(S[:-1], S[1:])):
    if l == "R" and r == "L":
        goal.append(i)

ans = [0] * N

p = 0
for i in range(0, len(rle), 2):
    _, nl = rle[i]
    _, nr = rle[i + 1]
    g = goal[i // 2]
    ans[g] += (nl + 1) // 2
    ans[g + 1] += nl // 2
    ans[g + 1] += (nr + 1) // 2
    ans[g] += nr // 2

print(*ans)
