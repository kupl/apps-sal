
def f(A, N, M, Q, conditions):
    L = len(A) - 1

    if L > N:
        return

    elif L < N:
        fans = 0
        for j in range(A[L], M + 1):
            fans = max(fans, f(A + [j], N, M, Q, conditions))

    else:
        fans = 0
        for i in range(Q):
            a, b, c, d = conditions[i]
            if A[b] - A[a] == c:
                fans += d

    return fans


N, M, Q = [int(x) for x in input().split()]

conditions = []
for i in range(Q):
    c = [int(x) for x in input().split()]
    conditions.append(c)

ans = f([1], N, M, Q, conditions)

print(ans)
