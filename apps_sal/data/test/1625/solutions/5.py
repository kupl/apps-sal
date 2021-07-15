def arr_inp():
    return [float(x) for x in input().split()]


def solve(n):
    nonlocal s
    if n == 1:
        s += a[0]
        return
    else:
        solve(n // 4)
    s += sum(a[:n])


n, a, s = int(input()), arr_inp(), 0
a = sorted(a, reverse=True)
solve(n)
print(int(s))

