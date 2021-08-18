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


n, a, s = int(input()), sorted(arr_inp(), reverse=True), 0
solve(n)
print(int(s))
