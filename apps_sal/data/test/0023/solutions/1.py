fact_ = [1] * 50


def fact(n):
    return fact_[n]


def get_perm(n, k):
    if k > fact(n):
        exit(123)

    if n == 1:
        return [1]

    k -= 1
    res = []
    not_used = [i for i in range(1, n + 1)]
    size = fact(n - 1)
    for i in range(n):
        cnt = k // size
        res.append(not_used[cnt])
        not_used.pop(cnt)
        k %= size
        if i != n - 1:
            size //= (n - 1 - i)
    return res[::]


def num_by_perm(x):
    nonlocal n, a
    v = get_perm(n, x)
    res = []
    for i in range(n):
        res.append(a[v[i] - 1])
    return int(''.join(res))


def check(x):
    nonlocal n, a, b
    v = num_by_perm(x)
    if v > b:
        return False
    else:
        return True


for i in range(1, 20):
    fact_[i] = fact_[i - 1] * i


a = list(input())
b = int(input())
n = len(a)

a.sort()

l = 1
r = fact(n) + 1
while r - l > 1:
    m = l + (r - l) // 2
    if check(m):
        l = m
    else:
        r = m

print(num_by_perm(l))

