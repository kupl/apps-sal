def f(n, k, l, r):
    if n & 1:
        if k == n:
            return bool(l & 1)
        elif k & 1:
            return n + k <= 2 * l
        else:
            return 2 * l < n + k and 2 * l > n - k - 1
    else:
        if k == n:
            return bool(l & 1)
        elif k & 1:
            return n - k + 1 <= 2 * l
        else:
            return False

n, k = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

l = list([i & 1 for i in a]).count(1)
r = n - l

print('Stannis' if f(n, k, l, r) else 'Daenerys')

