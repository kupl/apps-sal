N, M = map(int, input().split())

A_list = []
for _ in range(N):
    A = list(map(int, input().split()))
    del A[0]
    A_list.extend(A)

ans = 0
for i in range(1, M + 1):
    if A_list.count(i) == N:
        ans += 1

print(ans)
