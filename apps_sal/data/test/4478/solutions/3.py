m = int(input())
a = []
for i in range(m):
    n = int(input())
    a.append(list(map(int, input().split())))
d = dict()
f = 0
for i in range(m):
    summ = sum(a[i])
    for j in range(len(a[i])):
        if(summ - a[i][j] in d):
            if(d[summ - a[i][j]][0] != i + 1):
                print("YES")
                print(*d[summ - a[i][j]])
                print(i + 1, j + 1)
                f = 1
                break
        d[summ - a[i][j]] = [i + 1, j + 1]
    if(f):
        break
if(f == 0):
    print("NO")
