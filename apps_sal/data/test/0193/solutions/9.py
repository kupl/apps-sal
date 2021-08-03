store1 = input("").split(' ')
a = int(store1[0])
b = int(store1[1])
store2 = input("").split(' ')
c = int(store2[0])
d = int(store2[1])
lo = 0
hi = 2 * 10**18
while (hi - lo > 10**-9 * lo):
    mid = (hi + lo) / 2.0
    mini = 2 * 10**19
    maxi = -2 * 10**19
    for t in range((1 << 4)):
        store = [a, b, d, c]
        for k in range(4):
            if (((1 << k) & t) != 0):
                store[k] += mid
            else:
                store[k] -= mid
        x = store[0] * store[2] - store[1] * store[3]
        if (x >= maxi):
            maxi = x
        if (x <= mini):
            mini = x
    if (mini <= maxi and maxi >= 0 and mini <= 0):
        hi = mid
    else:
        lo = mid
print(lo)
