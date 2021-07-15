n, m, x, y = map(int, input().split())
print(x, y)
for i in range(1, m + 1):
    if i  != y:
        print(x, i)
t = False
for i in range(1, n + 1):
    if i != x:
        if t:
            for j in range(1, m + 1):
                print(i, j)
        else:
            for j in range(m, 0, -1):
                print(i, j)
                
        t = not t
