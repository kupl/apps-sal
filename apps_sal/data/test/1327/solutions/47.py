(n, m) = map(int, input().split())
p = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
cake = [list(map(int, input().split())) for i in range(n)]
ans = 0
for (a, b, c) in p:
    cou = []
    for (x, y, z) in cake:
        cou.append(x * a + y * b + z * c)
    cou.sort(reverse=True)
    ans = max(ans, sum(cou[:m]))
print(ans)
