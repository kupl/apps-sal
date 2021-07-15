import sys
n = int(input())
a = input()
b = input()
l = 0
c = [[0 for j in range(26)] for i in range(26)]
for i in range(n):
    if a[i] != b[i]:
        l += 1
        c[ord(a[i]) - ord('a')][ord(b[i]) - ord('a')] = i+1

for i in range(26):
    for j in range(26):
        if i == j or c[i][j] == 0 or c[j][i] == 0:
            continue
        print(l-2)
        print(c[i][j], c[j][i])
        return
for i in range(26):
    for j in range(26):
        if i == j or c[i][j] == 0 or max(c[j]) == 0:
            continue
        print(l-1)
        print(c[i][j], end=' ')
        for k in range(26):
            if c[j][k] > 0:
                print(c[j][k])
        return
print(l)
print(-1, -1)

