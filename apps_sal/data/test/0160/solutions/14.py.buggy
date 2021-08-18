import numpy as np


def divisors(num):
    array = []
    limit = int(num ** 0.5) + 1
    for i in range(1, limit):
        if num % i == 0:
            div1 = i
            div2 = num // i
            array.append(div1)
            if div1 != div2:
                array.append(div2)
    array.sort(reverse=True)
    return array


n, k = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype=int)

total = sum(A)
candidates = divisors(total)


for div in candidates:
    mods = A % div
    mods.sort()
    add = div - mods

    addcum = np.cumsum(add)
    subcum = np.cumsum(mods)
    for i in range(n):
        addcount = addcum[n - 1] - addcum[i]
        subcount = subcum[i]
        if addcount == subcount and addcount <= k:
            print(div)
            return
