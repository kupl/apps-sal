import collections
N = int(input())
S = int(input())


def prime_decomposition(n):
    i = 2
    ret = collections.defaultdict(int)
    while i * i <= n:
        while n % i == 0:
            n //= i
            ret[i] += 1
        i += 1
    if n > 1:
        ret[n] = 1
    return ret


def digitsum(x, f):
    if x < f:
        return x
    else:
        return x % f + digitsum(x // f, f)


if N == S:
    print((N + 1))
    return
fs_dict = prime_decomposition(N - S)
fs_set = set([1])
for p, n in list(fs_dict.items()):
    fs_set_copy = fs_set.copy()
    for i in range(1, n + 1):
        for x in fs_set_copy:
            fs_set.add(x * p**i)
for f in sorted(fs_set):
    f += 1
    if digitsum(N, f) == S:
        print(f)
        return
print((-1))
