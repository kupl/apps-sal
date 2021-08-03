n = int(input())
a = [int(input()) for i in range(n)]


def rec(s, a, i):
    if i == len(a):
        return (s % 360 == 0)
    return rec((s + a[i]) % 360, a, i + 1) or rec((s - a[i]) % 360, a, i + 1)


print('YES' if rec(0, a, 0) else 'NO')
