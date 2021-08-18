n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
f = 0
if 1 in l2:
    c = l2.index(1)
    d = 1
    for i in range(c, n):
        if l2[i] != d:
            break
        d += 1
    else:

        for k in range(c):
            if l2[k] != 0 and l2[k] - k <= d:
                break
        else:
            print(c)
            f = 1
if f == 0:
    s = -2
    for i in range(n):
        if l2[i] != 0:
            s = max(s, i - l2[i])
    print(n + s + 2)
