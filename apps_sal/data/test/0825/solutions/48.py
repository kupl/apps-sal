N = int(input())

if N == 1:
    print(0)
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


def p_num(m):
    ret = 0
    for j in range(1, 10**12):
        ret += j
        if ret <= m < ret + (j + 1):
            ans = j
            break
    return ans


p = factorization(N)

cnt = 0
for k in range(len(p)):
    cnt += p_num(p[k][1])
print(cnt)
