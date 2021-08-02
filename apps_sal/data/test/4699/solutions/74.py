def iparse():
    return list(map(int, input().split()))


n, k = iparse()
d = iparse()

for i in range(n, 5000000):
    tmp = i
    f = True
    while tmp > 0:
        x = tmp % 10
        if x in d:
            f = False
            break
        tmp //= 10
    if f:
        print(i)
        return
