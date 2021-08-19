N = int(input())
ret = 0
# L,Rを総当たりしたときの頂点数の総和
for i in range(N):
    ret += (i + 1) * (N - i)
for _ in range(N - 1):
    # 辺が1つ有効になるごに、連結成分が1つ減る
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x > y:
        x, y = y, x
    ret -= (x + 1) * (N - y)

print(ret)
