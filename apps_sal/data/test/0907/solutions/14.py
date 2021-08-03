from sys import stdin
"""
n=int(stdin.readline().strip())
n,m=map(int,stdin.readline().strip().split())
s=list(map(int,stdin.readline().strip().split()))
"""
n, m = list(map(int, stdin.readline().strip().split()))
s = [list(map(int, stdin.readline().strip().split())) for i in range(m)]
a, b = s[0][0], s[0][1]
s1 = []
flag = False
for i in range(len(s)):
    if s[i][0] != a and s[i][1] != a:
        s1.append(s[i])
a1 = 0
b1 = 0
for i in range(len(s1)):
    if i == 0:
        a1, b1 = s1[0][0], s1[0][1]

        continue
    if a1 != s1[i][1] and a1 != s1[i][0]:
        a1 = -1
    if b1 != s1[i][1] and b1 != s1[i][0]:
        b1 = -1

if b1 != -1 or a1 != -1:
    flag = True
s1 = []
for i in range(len(s)):
    if s[i][0] != b and s[i][1] != b:
        s1.append(s[i])
a1 = 0
b1 = 0
for i in range(len(s1)):
    if i == 0:
        a1, b1 = s1[0][0], s1[0][1]
        continue
    if a1 != s1[i][1] and a1 != s1[i][0]:
        a1 = -1
    if b1 != s1[i][1] and b1 != s1[i][0]:
        b1 = -1

if b1 != -1 or a1 != -1:
    flag = True

if flag:
    print("YES")
else:
    print("NO")
