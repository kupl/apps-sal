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


def product(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p


S, P = map(int, input().split())
a = factorization(P)
nums = [1]

for i in a:
    for _ in range(i[1]):
        nums.append(i[0])

n = len(nums)

for i in range(2 ** n):
    a = []
    b = []
    for j in range(n):
        if ((i >> j) & 1):
            a.append(nums[j])
        else:
            b.append(nums[j])

    N = product(a)
    M = product(b)

    if N > 0 and M > 0:
        if N + M == S:
            print("Yes")
            return

print("No")
