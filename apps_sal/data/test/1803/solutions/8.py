import sys
my_file = sys.stdin
n = int(my_file.readline().strip('\n'))
a = [int(i) for i in my_file.readline().strip('\n').split()]
m = int(my_file.readline().strip('\n'))
x = []
y = []
for i in range(m):
    line = [int(k) for k in my_file.readline().strip('\n').split()]
    x.append(line[0] - 1)
    y.append(line[1])
for (x, y) in zip(x, y):
    try:
        if x - 1 >= 0:
            a[x - 1] += y - 1
    except:
        pass
    try:
        if x + 1 < n:
            a[x + 1] += a[x] - y
    except:
        pass
    a[x] = 0
for i in a:
    print(i)
