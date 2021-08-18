from collections import defaultdict

N, K, L = list(map(int, input().split()))


root_road = [-1] * N
root_train = [-1] * N


def find_road(x):
    if root_road[x] < 0:
        return x

    root_road[x] = find_road(root_road[x])
    return root_road[x]


def union_road(x, y):
    x = find_road(x)
    y = find_road(y)
    if x == y:
        return

    root_road[x] += root_road[y]
    root_road[y] = x


def same_road(x, y):
    return find_road(x) == find_road(y)


def find_train(x):
    if root_train[x] < 0:
        return x

    root_train[x] = find_train(root_train[x])
    return root_train[x]


def union_train(x, y):
    x = find_train(x)
    y = find_train(y)
    if x == y:
        return

    root_train[x] += root_train[y]
    root_train[y] = x


def same_train(x, y):
    return find_train(x) == find_train(y)


dc = defaultdict(list)
dt = defaultdict(list)
for _ in range(K):
    p, q = list(map(int, input().split()))
    p -= 1
    q -= 1
    dc[p].append(q)
    dc[q].append(p)
    union_road(p, q)

for _ in range(L):
    r, s = list(map(int, input().split()))
    r -= 1
    s -= 1
    dt[r].append(s)
    dt[s].append(r)
    union_train(r, s)

dic = {}
for i in range(N):
    if (find_road(i), find_train(i)) not in dic:
        dic[(find_road(i), find_train(i))] = 1
        continue
    else:
        dic[(find_road(i), find_train(i))] += 1

ans = []
for i in range(N):
    ans.append(dic[(find_road(i), find_train(i))])
print((*ans))
