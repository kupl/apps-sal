n = int(input())
a = [(-x - 1, x)[x < 0] for x in map(int, input().split())]
if n % 2:
    m = min(a)
    i = a.index(m)
    a[i] = -a[i] - 1
print(*a)
