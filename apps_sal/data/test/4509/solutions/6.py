def f(x, n):
    return x // n

def ff(l, r, n):
    return f(r, n) - f(l - 1, n)

for _ in range(int(input())):
    # n = int(input())
    # arr = list(map(int, input().split()))
    n, k = list(map(int, input().split()))
    k -= 1
    s = 1
    while k > 0:
        nk = ff(s, s + k, n)
        s += k
        k = nk
        if s % n == 0:
            s -= 1
        if k == 1:
            k = 0
            s += 1
            if s % n == 0:
                s += 1

    print(s)

