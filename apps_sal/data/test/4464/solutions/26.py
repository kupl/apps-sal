import copy
(a, b, c) = map(int, input().split())
x = copy.deepcopy(a)
visited = [False] * (b + 1)
flg = True
while True:
    x %= b
    if x == c:
        break
    elif visited[x]:
        flg = False
        break
    else:
        visited[x] = True
        x += a
print('YES') if flg else print('NO')
