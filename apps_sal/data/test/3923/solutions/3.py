n, a, b = list(map(int, input().strip().split()))


def pp(seq):
    return ' '.join(map(str, seq))


def cycle(start, size):
    return list(range(start + 1, start + size)) + [start]


def fail_sequence(target, acc=[]):
    ''' recursion failure, bloody python '''

    if target % a == 0:
        return acc + [a] * (target // a)
    if target % b == 0:
        return acc + [b] * (target // b)

    if a <= target:
        acc.append(a)
        res = sequence(target - a, acc)
        if res:
            return res
        acc.pop()
    if b <= target:
        acc.append(b)
        return sequence(target - b, acc)
    return []


def sequence(target, a, b):
    dp = {0: (0, 0)}  # num of (a, b) needed to reach sum
    for i in range(1, target + 1):
        if i - a in dp:
            na, nb = dp[i - a]
            dp[i] = (na + 1, nb)
        elif i - b in dp:
            na, nb = dp[i - b]
            dp[i] = (na, nb + 1)
    na, nb = dp.get(target, (0, 0))
    return [a] * na + [b] * nb


def sol():
    seq = sequence(n, a, b)

    if seq:
        res = []
        i = 1
        for size in seq:
            res.extend(cycle(i, size))
            i += size
        return pp(res)
    else:
        return -1


print(sol())
