a, b = list(map(int, input().split()))
if a == 1 and b == 1:
    print((1))
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


ans = 0
A = factorization(a)
B = factorization(b)
for i in A:
    for j in B:
        if i[0] == j[0]:
            ans += 1
print((ans + 1))
