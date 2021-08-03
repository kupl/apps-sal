a, b, c = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
x, y, z, u = a[1] + a[2], b[0] + b[2], c[0] + c[1], a[2] + c[0]
t = (u + x + z) // 2
a[0], b[1], c[2] = t - x, t - y, t - z
print(' '.join(str(i) for i in a))
print(' '.join(str(i) for i in b))
print(' '.join(str(i) for i in c))
