n = int(input())
l = [int(x) for x in input().split()]
m = int(input())
for i in range(m):
    a, b = [int(x) for x in input().split()]
    if a != 1:
        l[a - 2] += b - 1
    if a != n:
        l[a] += l[a - 1] - b
    l[a - 1] = 0
for i in l:
    print(i)
