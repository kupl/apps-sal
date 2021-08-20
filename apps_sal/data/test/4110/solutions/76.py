(D, G) = [int(x) for x in input().split()]
(P, C) = ([], [])
for _ in range(D):
    (p, c) = [int(x) for x in input().split()]
    P.append(p)
    C.append(c)
ans = 1000
for b in range(2 ** D):
    score = 0
    solve = 0
    unsolved = []
    for i in range(D):
        if b >> i & 1:
            score += C[i] + 100 * (i + 1) * P[i]
            solve += P[i]
        else:
            unsolved.append(i)
    if G > score:
        resprbs = []
        unsolved.reverse()
        for i in unsolved:
            resprbs += [100 * (i + 1)] * (P[i] - 1)
        for j in range(len(resprbs)):
            score += resprbs[j]
            solve += 1
            if G <= score:
                break
    if G <= score:
        ans = min(ans, solve)
print(ans)
