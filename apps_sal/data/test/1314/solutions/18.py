N = int(input())
p, q = 0, 0
for i in range(N * 2):
    x, y = list(map(int, input().split()))
    p += x
    q += y

print(p // N, q // N)
