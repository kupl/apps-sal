n, a, b = list(map(int, input().split()))
v = ['2'] * n
for x in input().split():
    v[int(x) - 1] = '1'
print(' '.join(v))

