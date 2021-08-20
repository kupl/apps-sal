(N, M) = map(int, input().split())
(L, R) = ([], [])
for i in range(M):
    (x, y) = map(int, input().split())
    L.append(x)
    R.append(y)
(max_l, min_r) = (max(L), min(R))
print(max(0, min_r - max_l + 1))
