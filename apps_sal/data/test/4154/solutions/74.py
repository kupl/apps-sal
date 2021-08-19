(n, m) = map(int, input().split())
min_id = 0
max_id = 10 ** 9
for _ in range(m):
    (l, r) = map(int, input().split())
    min_id = max(l, min_id)
    max_id = min(r, max_id)
ans = max_id - min_id + 1
if ans <= 0:
    print(0)
else:
    print(ans)
