n, p = list(map(int, input().split()))
l = 1
k = 1
while n - l * p > 0:
    s = bin(n - l * p)[2:]
    l1 = 0
    l2 = 0
    last = 0
    for i in s:
        if i == "1":
            l1 += 1
            l2 += 1
            last = 1
        else:
            if last > 0:
                l2 += 2 ** (last - 1)
                last += 1
    if l >= l1 and l2 >= l:
        print(l)
        k = 0
        break
    l += 1
if k:
    print(-1)

