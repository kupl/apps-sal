from fractions import gcd
3


def main():
    n = int(input())
    m = list(map(int, input().split()))
    r = list(map(int, input().split()))
    k = 1
    for x in m:
        k = x * k // gcd(x, k)
    a = 0
    for i in range(k):
        f = 0
        for j in range(n):
            if i % m[j] == r[j]:
                f = 1
                break
        a += f
    print(a / k)


main()
