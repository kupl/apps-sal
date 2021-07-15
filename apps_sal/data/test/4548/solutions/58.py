n, m, x = map(int, input().split())
a = [int(s) for s in input().split()]

for i in range(m):
    if a[i] > x:
        less = len(a[:i])
        more = len(a[i:])
        print(min(less, more))
        break
