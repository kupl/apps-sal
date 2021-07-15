#!python3

# input
L = input()

MOD = 10 ** 9 + 7
MAX = 10 ** 5 + 5
p3 = [None] * MAX


def p3_init():
    p3[0] = 1
    for i in range(1, MAX):
        p3[i] = 3 * p3[i - 1] % MOD


def main():
    p3_init()
    n = len(L)
    w = 1
    ans = 0
    for i in range(n):
        if L[i] == "1":
            # 両方0にする場合
            ans = (ans + w * p3[n - i - 1]) % MOD
            # 片方1にする場合
            w = 2 * w % MOD
    ans = (ans + w) % MOD
    print(ans)


def __starting_point():
    main()

__starting_point()
