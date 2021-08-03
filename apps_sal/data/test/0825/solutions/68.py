n = int(input())


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


q = factorization(n)

ans = 0
for i in range(len(q)):
    l = q[i][1]
    if q[i][0] == 1:
        continue

    for j in range(1, l + 1):
        l -= j
        if l < 0:
            break
        else:
            ans += 1
print(ans)
