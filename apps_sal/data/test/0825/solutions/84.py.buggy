N = int(input())

if N == 1:
    print('0')
    return


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
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


def divcount(n):
    cnt = 0
    while n >= 0:
        n -= cnt + 1
        cnt += 1
    return cnt - 1


s = factorization(N)
t = [i[1] for i in s]
ans = 0
for i in t:
    ans += divcount(i)
print(ans)
