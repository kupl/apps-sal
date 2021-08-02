n = int(input())

respectingChildren = [0 for i in range(n)]
totalChildren = [0 for i in range(n)]
Ci = []
Pi = []
root = 0

for i in range(n):
    pi, ci = list(map(int, input().split()))
    Ci.append(ci)
    if pi == -1:
        Pi.append(pi)
        root = i
        continue

    Pi.append(pi - 1)
    totalChildren[pi - 1] += 1
    if ci == 0:
        respectingChildren[pi - 1] += 1

ans = []
for i in range(n):
    if i == root:
        continue

    if Ci[i] == 1:
        if respectingChildren[i] == 0:
            ans.append(i + 1)
            parentOfI = Pi[i]
            totalChildren[parentOfI] += totalChildren[i]

if ans == []:
    print(-1)
else:
    print(*ans)
