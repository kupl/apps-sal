(A, B) = map(int, input().split())


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
    return arr


facts_A = factorization(A)
cnt = 0
for l in facts_A:
    if B % l[0] == 0:
        cnt += 1
print(cnt + 1)
