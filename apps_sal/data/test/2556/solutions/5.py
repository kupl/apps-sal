n = int(input())
for i in range(n):
    c, s = list(map(int, input().strip().split()))
    left = s % c
    v = s // c
    o = 0
    for i in range(left):
        o += (v + 1) ** 2
    for i in range(left, c):
        o += v ** 2
    print(o)
