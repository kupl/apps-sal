v = int(input())
for i in range(v):
    a = [int(x) for x in input().split()]
    c = a[0] * a[1]
    if c % 2 == 1:
        c += 1
    print(int(c / 2))
