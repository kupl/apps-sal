n = int(input())
pl = [0] * 100
p = [[] for i in range(100)]
s = [str() for i in range(100)]
cp = [0] * 100
rp = [0] * 100
X = 0
Y = 0
for i in range(n):
    s[i] = str(input())
    f = 0
    for j in range(len(s[i])):
        if s[i][j] == '.':
            f = 1
            break
    if f == 0:
        X = 1
for i in range(n):
    f = 0
    for j in range(n):
        if s[j][i] == '.':
            f = 1
            break
    if f == 0:
        Y = 1
if X == 1 and Y == 1:
    print('-1')
elif X == 0:
    for i in range(n):
        for j in range(n):
            if s[i][j] == '.':
                print(i + 1, j + 1)
                break
else:
    for i in range(n):
        for j in range(n):
            if s[j][i] == '.':
                print(j + 1, i + 1)
                break
