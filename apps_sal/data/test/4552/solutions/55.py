N = int(input())
F = []
for i in range(N):
    A = list(map(int, input().split()))
    F.append(A[::-1])

P = []
for i in range(N):
    A = list(map(int, input().split()))
    P.append(A)

result = float("inf")*(-1)
for i in range(1, 2**10):
    ans = 0
    for l in range(N):
        c = 0
        for j in range(10):
            if ((i>>j) & 1):
                if F[l][j] == 1:
                    c += 1
        ans += P[l][c]
    result = max(ans, result)
print(result)

