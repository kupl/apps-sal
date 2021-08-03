n, x = list(map(int, input().split()))
l = [int(i) for i in input().split()]
p = 0
for i in range(n):
    p += l[i]
    if p > x:
        print((i + 1))
        break
else:
    print((n + 1))
