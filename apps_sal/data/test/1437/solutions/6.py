def main():

    def f1(c):
        x = ord(c)
        if ord('0') <= x <= ord('9'):
            res = int(c)
        elif ord('A') <= x <= ord('Z'):
            res = x - ord('A') + 10
        elif ord('a') <= x <= ord('z'):
            res = x - ord('a') + 36
        elif c == '-':
            res = 62
        elif c == '_':
            res = 63
        return res

    def f2(x):
        res = bin(x)[2:]
        res = '0' * (6 - len(res)) + res
        return res

    def read():
        return list(map(int, input().split()))
    s = input()
    mod = 10 ** 9 + 7
    n = len(s)
    a = [f2(f1(i)) for i in s]
    t = ''.join(a)
    p = t.count('0')
    ans = 3 ** p % mod
    print(ans)


main()
