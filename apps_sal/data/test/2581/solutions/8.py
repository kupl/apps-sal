
from sys import stdin
input = stdin.buffer.readline
n = int(input())
ans = []

for _ in range(n):
    arr = list(map(int,input().split()))
    ans.append(arr)

topLeft, bottomLeft = {}, {}

for i in range(n):
    for j in range(n):
        topLeft[i-j] = topLeft.get(i-j, 0) + ans[i][j]
        bottomLeft[i+j] = bottomLeft.get(i+j, 0) + ans[i][j]

mx1, mx2, pos1, pos2 = -1, -1, [-1,-1], [-1,-1]

for i in range(n):
    for j in range(n):
        if (i+j) & 1:
            if mx1 < topLeft[i-j] + bottomLeft[i+j] - ans[i][j]:
                mx1, pos1 = topLeft[i-j] + bottomLeft[i+j] - ans[i][j], [i+1,j+1]
        else:
            if mx2 < topLeft[i - j] + bottomLeft[i + j] - ans[i][j]:
                mx2, pos2 = topLeft[i - j] + bottomLeft[i + j] - ans[i][j], [i+1, j+1]

print(mx1+mx2)
print(pos1[0], pos1[1], pos2[0], pos2[1])

