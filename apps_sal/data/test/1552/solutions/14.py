n = int(input())
b = [[] for i in range(3)]
a = [int(x) for x in input().split(' ')]
for i in range(n):
    b[a[i] - 1].append(i + 1)
m = min(len(b[0]), len(b[1]), len(b[2]))
print(m)
for i in range(m):
    print(b[0][i], b[1][i], b[2][i], sep=' ')
