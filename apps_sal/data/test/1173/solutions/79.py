from collections import defaultdict
N = int(input())
a = [[0 for j in range(N - 1)] for i in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N - 1):
        a[i][j] = line[j] - 1
    a[i] = a[i][::-1]

q = []


def check(i):
    if len(a[i]) == 0:
        return False
    j = a[i][-1]
    if a[j][-1] == i:
        q.append([i, j])


for i in range(N):
    check(i)


day = 0
while q:
    day += 1
    prevQ = q.copy()
    q = []
    matched = defaultdict(list)
    for p in prevQ:
        i = p[0]
        j = p[1]
        if i > j:
            i, j = j, i
        if matched[i]:
            continue
        a[i].pop()
        a[j].pop()
        check(i)
        check(j)
        matched[i].append(j)

for i in range(N):
    if len(a[i]) != 0:
        print((-1))
        break
else:
    print(day)
