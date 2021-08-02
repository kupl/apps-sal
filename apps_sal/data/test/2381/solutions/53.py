MOD = 10**9 + 7


def prod(a):
    res = 1
    for x in a:
        res = (res * x) % MOD
    return res


def solve(n, k, a):
    if k == 1:
        return max(a)
    elif k == n:
        return prod(a)
    elif (max(a) < 0) and (k % 2 == 1):
        a = sorted(a, reverse=True)
        return prod(a[:k])
    else:
        a = sorted(a, key=lambda x: -abs(x))
        num_negative = len(list([x for x in a[:k] if x < 0]))
        if num_negative % 2 == 0:
            return prod(a[:k])
        else:
            i1, j1 = None, None
            for i in range(k):
                if a[i] < 0:
                    i1 = i
            for j in range(k, n):
                if a[j] >= 0:
                    j1 = j
                    break
            i2, j2 = None, None
            for i in range(k):
                if a[i] >= 0:
                    i2 = i
            for j in range(k, n):
                if a[j] < 0:
                    j2 = j
                    break
            if (i1 is None) or (j1 is None):
                return prod(a[:i2] + a[i2 + 1:k] + [a[j2]])
            elif (i2 is None) or (j2 is None):
                return prod(a[:i1] + a[i1 + 1:k] + [a[j1]])
            elif abs(a[j1] * a[i2]) > abs(a[i1] * a[j2]):
                return prod(a[:i1] + a[i1 + 1:k] + [a[j1]])
            else:
                return prod(a[:i2] + a[i2 + 1:k] + [a[j2]])


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
print((solve(n, k, a)))
