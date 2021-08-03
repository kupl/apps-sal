N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    tmp = 0
    for a, b in zip(A[i], B):
        tmp += a * b
    tmp += C
    if tmp > 0:
        ans += 1
print(ans)
