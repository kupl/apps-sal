def sing(n, t, k):
    have = 0
    q = [t]
    last = 0

    while have < n:
        last = q[0]
        q.append(q[0] + t)
        q = q[1:]
        have += k

        q.sort()

    return last


def getdouble(n, t, k, d):
    have = 0
    q = [t, d + t]
    last = 0

    while have < n:
        last = q[0]
        q.append(q[0] + t)
        q = q[1:]
        have += k

        q.sort()

    return last


def main():
    n, t, k, d = list(map(int, input().split()))
    single = (n + k - 1) // k
    single *= t
    single = sing(n, t, k)
    double = getdouble(n, t, k, d)

    print('YES' if double < single else 'NO')


main()
