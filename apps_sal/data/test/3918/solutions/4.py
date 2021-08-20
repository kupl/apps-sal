(N, K1, K2) = map(int, input().split())
(A, B) = ([*map(int, input().split())], [*map(int, input().split())])
for i in range(K1):
    (max_pos, max_diff) = (-1, 0)
    for j in range(N):
        if abs(A[j] - B[j]) >= max_diff:
            (max_pos, max_diff) = (j, abs(A[j] - B[j]))
    if A[max_pos] >= B[max_pos]:
        A[max_pos] -= 1
    else:
        A[max_pos] += 1
for i in range(K2):
    (max_pos, max_diff) = (-1, 0)
    for j in range(N):
        if abs(A[j] - B[j]) >= max_diff:
            (max_pos, max_diff) = (j, abs(A[j] - B[j]))
    if B[max_pos] >= A[max_pos]:
        B[max_pos] -= 1
    else:
        B[max_pos] += 1
ans = 0
for i in range(N):
    ans += (A[i] - B[i]) ** 2
print(ans)
