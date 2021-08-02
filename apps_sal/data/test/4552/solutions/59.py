n = int(input())

F = []
P = []
for i in range(n):
    F.append(list(map(int, input().split())))
for i in range(n):
    P.append(list(map(int, input().split())))
ans = -10**9
for i in range(1, 1 << (10)):
    C = [0] * n
    for j in range(10):
        if i & 2**j:
            for k in range(n):
                if F[k][j]:
                    C[k] += 1
    current = 0
    for k in range(n):
        current += P[k][C[k]]
    ans = max(current, ans)
print(ans)
