n = int(input())
x = [input().split() for i in range(n)]
for i in range(n):
    x[i][1] = int(x[i][1])
    x[i].append(i+1)

x.sort(key= lambda a: a[1])
x.reverse()
x.sort(key= lambda b: b[0])

for i in range(n):
    print(x[i][2])
