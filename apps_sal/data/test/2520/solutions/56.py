(N, M, K) = list(map(int, input().split()))
p = [0] * N
for i in range(N):
    p[i] = [0] * 3
    p[i][0] = []
    p[i][1] = []
    p[i][2] = -1
g = []
stack = []
groupNum = 0
fcs = []
for i in range(M):
    (a, b) = list(map(int, input().split()))
    p[a - 1][0].append(b - 1)
    p[b - 1][0].append(a - 1)


def groupmake(person, group):
    groupSize = 0
    stack.append(person)
    p[person][2] = group
    while True:
        num = stack.pop()
        groupSize += 1
        for i in p[num][0]:
            if p[i][2] == -1:
                stack.append(i)
                p[i][2] = group
        if len(stack) == 0:
            return groupSize


for i in range(len(p)):
    if p[i][2] == -1:
        g.append(groupmake(i, groupNum))
        groupNum += 1
for person in p:
    fcs.append(g[person[2]] - len(person[0]) - 1)
for i in range(K):
    (c, d) = list(map(int, input().split()))
    if p[c - 1][2] == p[d - 1][2]:
        fcs[c - 1] -= 1
        fcs[d - 1] -= 1
print(' '.join(map(str, fcs)))
