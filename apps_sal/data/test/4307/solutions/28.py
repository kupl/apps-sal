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


factorization(25)
N = int(input())
N_list = [i for i in range(1, N + 1) if i % 2 == 1]
count = 0
for n in N_list:
    factor_list = factorization(n)
    num_divisor = 1
    for factor in factor_list:
        num_divisor *= factor[1] + 1
    if num_divisor == 8:
        count += 1
print(count)
