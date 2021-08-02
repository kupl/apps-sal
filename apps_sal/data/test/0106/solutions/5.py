def f(a, b):
    return min(abs(a - b) * 5, abs(a - b) + 10)


def main():
    n, m, k = map(int, input().split())
    a, b = map(int, input().split())
    pa, pb = (a - 1) // (m * k), (b - 1) // (m * k)
    ans = min((pa - pb + n) % n, (-pa + pb + n) % n) * 15
    ea, eb = (a - 1) // k % m, (b - 1) // k % m
    if ans == 0:
        ans = f(ea, eb)
    else:
        ans += f(ea, 0) + f(eb, 0)
    print(ans)


main()
