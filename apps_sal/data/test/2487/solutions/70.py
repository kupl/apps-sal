n = int(input())
ans = 0
for i in range(1, n + 1):  # 頂点数の総和を求める
    ans += i * (n - i + 1)
for _ in range(n - 1):  # 各辺についてu*(n-v+1)を頂点数の総和から引く
    u, v = map(int, input().split())
    if u > v:  # 上記ではu<vを仮定しているのでu>vのときuとvを入れ替える
        u, v = v, u
    ans -= u * (n - v + 1)
print(ans)
