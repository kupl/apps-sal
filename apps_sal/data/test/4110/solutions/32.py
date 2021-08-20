(D, G) = map(int, input().split())
P = []
C = []
for _ in range(D):
    (p, c) = map(int, input().split())
    P.append(p)
    C.append(c)
ans = []
for bit in range(1 << D):
    total_score = 0
    solved = 0
    for i in range(D):
        if bit & 1 << i:
            total_score += C[i] + (i + 1) * 100 * P[i]
            solved += P[i]
    for i in range(D - 1, -1, -1):
        if G <= total_score:
            ans.append(solved)
            break
        if bit & 1 << i:
            continue
        s = (i + 1) * 100
        required_score = G - total_score
        required_problem = (required_score + s - 1) // s
        total_score += min(required_problem, P[i] - 1) * s
        solved += min(required_problem, P[i] - 1)
        if G <= total_score:
            ans.append(solved)
        break
print(min(ans))
