N = int(input())


def divisor(x):
    div = []
    for i in range(1, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            div.append(i)
            if i != x // i:
                div.append(x // i)
    return sorted(div)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n ** (1 / 2)) + 1):
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


zt = [1]
ans = 0
while N > 1:
    for i in divisor(N):
        if i not in zt:
            if len(factorization(i)) == 1:
                z = i
                zt.append(z)
                break
    if z == 0:
        break
    N = N // z
    ans += 1
    z = 0
print(ans)
