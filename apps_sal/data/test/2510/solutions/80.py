n, m = list(map(int, input().split()))
# friend array
f = [i for i in range(n)]

# 友だち集合の中で最小IDを返す
def find(x):
    if f[x] == x:
        return x
    ret = find(f[x])
    f[x] = ret
    return ret

# 友だち集合を作る
def union(x, y):
    i, j = find(x), find(y)
    f[max(i, j)] = min(i, j)

for _ in range(m):
    a, b = list(map(int, input().split()))
    a, b = a-1, b-1
    union(a, b)

cnt = [0 for _ in range(n)]
for i in range(n):
    cnt[find(i)] += 1
print((max(cnt)))

