n, m = [int(i) for i in input().split()]
c = n
for i in range(m):
    a, b = [int(i) for i in input().split()]
    c = min(b-a+1, c)
print(c)
for i in range(n):
    print(i%c, end= ' ')
