n = int(input())
for i in range(n):
    a = int(input())
    f = [int(x) for x in input().split()]
    b = int(input())
    g = [int(x) for x in input().split()]
    odd1 = 0
    even1 = 0
    for h in range(a):
        if f[h] % 2 == 0:
            even1 += 1
    odd1 = a - even1
    odd2 = 0
    even2 = 0
    for h in range(b):
        if g[h] % 2 == 0:
            even2 += 1
    odd2 = b - even2
    print(odd2 * odd1 + even1 * even2)
