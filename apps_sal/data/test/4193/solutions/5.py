a = [input().split() for _ in range(3)]
n = int(input())
b = [input() for _ in range(n)]
a1 = []
for i in range(3):
    a1.append(a[0][i])
for i in range(3):
    a1.append(a[1][i])
for i in range(3):
    a1.append(a[2][i])
for i in range(n):
    if b[i] in a1:
        w = a1.index(b[i])
        a1[w] = 'a'
    else:
        pass
if a1[0] == a1[1] == a1[2] == 'a' or a1[3] == a1[4] == a1[5] == 'a' or a1[6] == a1[7] == a1[8] == 'a':
    print('Yes')
elif a1[0] == a1[3] == a1[6] == 'a' or a1[1] == a1[4] == a1[7] == 'a' or a1[2] == a1[5] == a1[8] == 'a':
    print('Yes')
elif a1[0] == a1[4] == a1[8] == 'a' or a1[2] == a1[4] == a1[6] == 'a':
    print('Yes')
else:
    print('No')
