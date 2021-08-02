t = int(input())
for i in range(t):
    n, s, k = list(map(int, input().split()))
    k = list(map(int, input().split()))
    l = dict()
    for i in k:
        l[i] = 1

    for i in range(1005):
        i1 = s + i
        i2 = s - i
        if (i2 > 0):
            if i2 not in l:
                print(i)
                break
        if (i1 <= n):
            if i1 not in l:
                print(i)
                break
