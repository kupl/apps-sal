N = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
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


l_2d = factorization(N)
cnt = 0
for l in l_2d:
    p = l[0]
    e = l[1]
    if p == 1:
        continue
    for i in range(1, 10 ** 7):
        if e < i:
            break
        cnt += 1
        e -= i
print(cnt)
