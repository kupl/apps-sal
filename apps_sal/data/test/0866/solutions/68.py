M = 10**9 + 7


def combination(n, k):
    if k > n - k:
        k = n - k
    p = [-1 for i in range(k + 1)]
    kp = {i: [] for i in range(n - k + 1, n + 1)}
    for i in range(2, k + 1):
        if p[i] != -1:
            continue
        for j in range(i, k + 1, i):
            if p[j] == -1:
                p[j] = i
        for j in range(((n - k) // i + 1) * i, n + 1, i):
            kp[j].append(i)
    count = [0 for i in range(k + 1)]
    for x in range(2, k + 1):
        buf = x
        while p[buf] != -1:
            m = p[buf]
            while buf > 1 and buf % m == 0:
                count[m] += 1
                buf = buf // m
    ans = 1
    for x in range(n - k + 1, n + 1):
        buf = x
        for i in kp[x]:
            while count[i] > 0 and buf % i == 0:
                buf = buf // i
                count[i] -= 1
        ans *= buf
        ans %= M
    return ans


X, Y = list(map(int, input().split()))
a = X + Y
b = a // 3
a = a % 3
# print(a,b)
if a == 0 and b <= X <= b * 2:
    print((combination(b, X - b)))
else:
    print((0))
