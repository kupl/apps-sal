N, M = list(map(int, input().split()))
root = [i for i in range(N)]
height = [0] * N


def find(a):
    f = a
    if a == root[a]:
        return a
    while a != root[a]:
        a = root[a]
    root[f] = a
    return a


def union(a, b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    if height[A] > height[B]:
        root[B] = root[A]
    else:
        root[A] = root[B]
        if height[A] == height[B]:
            height[B] += 1


for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    union(a, b)
l = [0] * N
for j in range(N):
    l[find(j)] += 1
print(N - l.count(0))
