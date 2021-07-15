mod = 10 ** 9 + 7


def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    f1 = 1
    f2 = 2
    for _ in range(n - 2):
        f1, f2 = f2, f1 + f2
        f2 %= mod
    return f2


def main():
    n = int(input())
    Caa = input()
    Cab = input()
    Cba = input()
    Cbb = input()
    if n == 2 or n == 3:
        return 1

    if Cab == "A":
        if Caa == "A":
            return 1
        if Cba == "A":
            return fibo(n - 2)
        return pow(2, n - 3, mod)
    elif Cab == "B":
        if Cbb == "B":
            return 1
        elif Cba == "B":
            return fibo(n - 2)
        return pow(2, n - 3, mod)


print(main())
