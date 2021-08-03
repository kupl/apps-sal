n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))


def buy(k):
    nonlocal n, s, arr
    if k == 0:
        return 0
    temp = sorted([arr[i - 1] + i * k for i in range(1, n + 1)])
    return sum(temp[:k])


def main():

    f, l = 0, n
    while f < l:
        if f == l - 1:
            a, b = buy(f), buy(l)
            return (l, b) if b <= s else (f, a)
        m = (f + l) // 2
        if buy(m) <= s:
            f = m
        else:
            l = m


a, b = main()
print(a, b)
