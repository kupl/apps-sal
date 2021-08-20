(N, M) = map(int, input().split())
Q = [tuple(map(int, input().split())) for _ in range(M)]
Q = sorted(Q, key=lambda x: x[1])
border = []
for (a, b) in Q:
    flag = True
    for x in border:
        if a < x and x <= b:
            flag = False
            break
    if flag:
        border.append(b)
ans = len(border)
print(ans)
