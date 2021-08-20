N = int(input())
mod = 10 ** 9 + 7


def factorization(n):
    (arr, temp) = ([], n)
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


A = {}
for i in range(1, N + 1):
    arr = factorization(i)
    for (k, v) in arr:
        if k != 1:
            if k not in A:
                A[k] = v
            else:
                A[k] += v
ans = 1
for v in A.values():
    ans *= v + 1
    ans %= mod
print(ans)
