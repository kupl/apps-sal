(N, M) = list(map(int, input().split()))
A = [[] for _ in range(N + 1)]
for _ in range(M):
    (a, b) = list(map(int, input().split()))
    A[a].append(b)
ans = False
for i in A[1]:
    if i == N:
        ans = True
        break
    for j in A[i]:
        if j == N:
            ans = True
            break
print('POSSIBLE' if ans else 'IMPOSSIBLE')
