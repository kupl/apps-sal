q = int(input())
for i in range(q):
    h, n = input().split()
    h = int(h)
    n = int(n)
    p = [int(j) for j in input().split()]+[0]
    s = 1
    a = 0
    for i in range(len(p)-1):
        if p[i]-p[i+1] >= 2 and s % 2 == 0:
            a += 1
            s = 2
        elif p[i]-p[i+1] >= 2 and s % 2 == 1:
            s = 2
        else:
            s += 1
    print(a)

