import bisect
n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
flag = 0
for i in range(0, n):
    for j in range(0, 31):
        b = a[i] + 2**j
        p = bisect.bisect_left(a, b)
        if p < n:
            if a[p] == b:
                a1 = a[i]
                b1 = b
                flag = 100
                c = a[i] + 2 * 2**j
                q = bisect.bisect_left(a, c)
                if q < n:
                    if a[q] == c:
                        flag = 200
                        break
    if flag == 200:
        break
if flag == 0:
    print(1)
    print(a[0])
elif flag == 100:
    print(2)
    print(a1, b1)
else:
    print(3)
    print(a[i], b, c)
