t = int(input())
for t in range(t):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    b = [0]
    for i in range(n):
        b.append(b[-1] + a[i])
    mn = b[0]
    for x in b:
        mn = min(mn, x)
    print(abs(mn))
