from math import gcd
A, B = map(int, input().split())


def factorize(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5) + 1):
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


n = gcd(A, B)
ans = factorize(n)
if ans[0][0] == 1:
    print(1)
    return
print(len(ans) + 1)
