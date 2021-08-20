import sys
input = sys.stdin.readline


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = {}
    f = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = b[i]
            f[a[i]] = 1
        else:
            d[a[i]] += b[i]
            f[a[i]] += 1
    ans = 0
    used = [0] * n
    for i in list(f.keys()):
        if f[i] > 1:
            for j in range(n):
                if i | a[j] == i and (not used[j]):
                    used[j] = 1
    for i in range(n):
        if used[i]:
            ans += b[i]
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
