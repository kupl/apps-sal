X, Y, A, B, C = map(int, input().split())
P = sorted(map(int, input().split()), reverse=True)[:X]
Q = sorted(map(int, input().split()), reverse=True)[:Y]
R = sorted(map(int, input().split()), reverse=True)[:X + Y]
i, j = X - 1, Y - 1
for r in R:
    if i == -1 and j == -1:
        break
    elif j == -1:
        if r > P[i]:
            P[i] = r
            i -= 1
        else:
            break
    elif i == -1:
        if r > Q[j]:
            Q[j] = r
            j -= 1
        else:
            break
    elif P[i] > Q[j]:
        if r > Q[j]:
            Q[j] = r
            j -= 1
        else:
            break
    else:
        if r > P[i]:
            P[i] = r
            i -= 1
        else:
            break
print(sum(P) + sum(Q))
