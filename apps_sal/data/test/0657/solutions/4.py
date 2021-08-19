(A, B) = list(map(int, input().split()))
(x, y, z) = list(map(int, input().split()))
need_a = 2 * x + 1 * y + 0 * z
need_b = 1 * y + 3 * z
print(max(0, need_a - A) + max(0, need_b - B))
