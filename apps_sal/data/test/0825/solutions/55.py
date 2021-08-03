import math
n = int(input())


def fac(n):
    arr = []
    temp = n
    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


l = fac(n)
if n == 1:
    print((0))
else:
    ans = 0
    for i in range(len(l)):
        count = l[i][1]
        p = 0
        k = 1
        while count > 0:
            if count - k < 0:
                break
            p += 1
            count -= k
            k += 1
        ans += p
    print(ans)
