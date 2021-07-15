N, M = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(set(a) & set(b)))

if c != []: print(c[0])
else: print(10 * min(a[0], b[0]) + max(a[0], b[0]))
