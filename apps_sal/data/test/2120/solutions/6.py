(n, m), f, s = list(map(int, input().split())), [int(x) for x in input().split()], 0

for i in range(m):
    (a, b) = list(map(int, input().split()))
    s = s + min(f[a - 1], f[b - 1])

print(s)
