n = int(input())
t = [int(x) for x in input().split()]


def check(t):
    t = sorted(set(t))
    for i in range(len(t) - 2):
        if (t[i + 1], t[i + 2]) == (t[i] + 1, t[i] + 2):
            return True
    return False


print('YES' if check(t) else 'NO')
