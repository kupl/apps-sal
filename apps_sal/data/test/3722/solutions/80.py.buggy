n = int(input())
mod = 10**9 + 7
c_aa = input()
c_ab = input()
c_ba = input()
c_bb = input()


def Fibo(n):
    cache = {}

    def impl(ni):
        nonlocal cache
        if ni <= 3:
            return 1
        if ni not in cache:
            cache[ni] = impl(ni - 2) + impl(ni - 1)
        return cache[ni]
    return impl(n)


if n <= 3:
    print(1)
    return
if c_ab == "B":
    if c_bb == "B":
        print(1)
        return
    if c_bb == "A":
        if c_ba == "A":
            print(2**(n - 3) % mod)
            return
        elif c_ba == "B":
            print(Fibo(n) % mod)
elif c_ab == "A":
    if c_aa == "A":
        print(1)
        return
    elif c_aa == "B":
        if c_ba == "B":
            print(2**(n - 3) % mod)
            return
        elif c_ba == "A":
            print(Fibo(n) % mod)
