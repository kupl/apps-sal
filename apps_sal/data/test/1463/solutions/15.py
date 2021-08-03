n = int(input())
a = [[0] * n for i in range(n)]
f = True
d = True
for i in range(n):
    a[i] = list(map(int, input().split(" ")))
for i in range(n):
    for j in range(n):
        s = a[i][j]

        if s != 1:
            f = False
            for t in range(n):
                if t != i:
                    x = s - a[t][j]
                    if x in a[i]:
                        f = True
        if f == False:
            d = False
if not d:
    print('No')
else:
    print('Yes')
