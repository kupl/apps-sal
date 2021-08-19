(r, c) = map(int, input().split())
a = [input() for i in range(r)]
t1 = set()
t2 = set()
for i in range(r):
    for j in range(c):
        if a[i][j] == 'S':
            t1.add(i)
            t2.add(j)
n = r - len(t1)
m = c - len(t2)
print(n * c + m * r - n * m)
