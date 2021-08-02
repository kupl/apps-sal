t = int(input())
for i10 in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    s = 0
    e = 0
    for i in range(n):
        if a[i] == 1:
            if e == 1:
                s += k
            e = 1
            k = 0
        else:
            k += 1
    print(s)
