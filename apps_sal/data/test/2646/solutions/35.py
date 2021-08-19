from collections import deque

# 入力:N,M(int:整数)


def input2():
    return map(int, input().split())

# 入力:[n1,n2,...nk](int:整数配列)


def input_array():
    return list(map(int, input().split()))


n, m = input2()
g = [[] for _ in range(n + 1)]  # 引数->要素で道しるべを保存
for i in range(m):
    a, b = input2()
    g[a].append(b)
    g[b].append(a)

q = deque()  # bfs用
q.append(1)  # 始点

check = [0] * (n + 1)  # 既に訪問している(1)か否(0)か
check[1] = 1

ans = [0] * (n + 1)  # 始点に近い側の，一つ前の要素(解答)
ans[1] = 1
for _ in range(10**5 + 1):
    if len(q) == 0:
        break
    v = q.popleft()  # 頂点を一つ取り出す
    for u in g[v]:  # vとの通路を全て探索
        if check[u] == 0:
            check[u] = 1  # 探索済み==1
            ans[u] = v
            q.append(u)
print("Yes")
for i in range(2, n + 1):
    print(ans[i])
