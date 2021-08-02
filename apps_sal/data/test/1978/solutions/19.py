

from collections import defaultdict


def bfs(root):
    bool = [False] * (n + 1)
    queue = [root]
    bool[root] = True
    level = defaultdict(int)
    level[root] = 0
    while queue:
        z = queue.pop(0)

        for i in hash[z]:
            if bool[i] == False:
                bool[i] = True
                level[i] += 1 + level[z]
                queue.append(i)

    return level


hash = defaultdict(list)
n = int(input())

l = []

for i in range(n):
    k = list(input())
    l.append(k)

for i in range(n):
    for j in range(n):
        if l[i][j] == '1':
            hash[i + 1].append(j + 1)
n1 = int(input())
la = list(map(int, input().split()))

root = la[0]


full = {}

for i in range(1, n + 1):
    full[i] = bfs(i)


ans = [la[0]]

j = 0

while j < len(la):

    k = j + 1

    while k < len(la):
        # print(k-)
        if full[la[j]][la[k]] == k - j:
            k += 1
        else:
            break

    # break
    if k == j:
        ans.append(la[j])
        j += 1
    else:
        ans.append(la[k - 1])
        j = k - 1
        if j == len(la) - 1:
            break


print(len(ans))
print(*ans)
