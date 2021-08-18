from itertools import product
n, m = list(map(int, input().split()))
xyz = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]


ans = 0
for a, b, c in product([1, -1], repeat=3):
    total = []
    for x, y, z in xyz:
        s = x * a + y * b + z * c
        total.append(s)
    total.sort(reverse=True)
    ans = max(ans, sum(total[:m]))
print(ans)
