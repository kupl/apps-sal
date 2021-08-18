S = input()
N = len(S)

curr = ["R", "L"]
idx = 0
cnt = 0
E = []
for i, ch in enumerate(S):
    if ch != curr[idx]:
        E.append((idx, cnt))
        cnt = 1
        idx = 1 - idx
    else:
        cnt += 1

E.append((idx, cnt))

ans = []
for i in range(0, len(E), 2):
    Rcnt = E[i][1]
    Lcnt = E[i + 1][1]
    Rfill = Lfill = (Rcnt + Lcnt) // 2

    if (Rcnt + Lcnt) % 2 == 1:
        if Rcnt % 2 == 1:
            Rfill += 1
        else:
            Lfill += 1

    for i in range(Rcnt - 1):
        ans.append(0)

    ans.append(Rfill)
    ans.append(Lfill)

    for i in range(Lcnt - 1):
        ans.append(0)


print(*ans, sep=" ")
