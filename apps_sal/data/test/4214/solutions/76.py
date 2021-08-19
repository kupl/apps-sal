import itertools
n = int(input())
p = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    (p[i][0], p[i][1]) = list(map(int, input().split()))


def dis(a, b):
    dis = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    return dis ** (1 / 2)


perm = [i for i in range(n)]
total = 0
num = 0
for v in itertools.permutations(perm, n):
    path = 0
    for i in range(n - 1):
        path += dis(p[v[i]], p[v[i + 1]])
    num += 1
    total += path
print(total / num)
