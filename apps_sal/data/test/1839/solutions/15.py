n = int(input())
a = []
b = []
for i in range(1, n*n+1):
    x, y = map(int, input().split())
    if x not in a and y not in b:
        print(i, end=' ')
        a.append(x)
        b.append(y)

