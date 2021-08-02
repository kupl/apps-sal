from math import sqrt


def Divisor_Set(n):
    s = set()
    for i in range(1, int(sqrt(n)) + 2):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s


def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a_sum = sum(a)
    st = Divisor_Set(a_sum)
    ans = 1
    st.remove(1)
    for v in st:
        b = [x % v for x in a]
        b.sort()
        for i in range(n - 1):
            b[i + 1] += b[i]
        for i in range(n - 1):
            if b[i] == v * (n - i - 1) - (b[-1] - b[i]):
                if b[i] <= k and ans < v:
                    ans = v
    print(ans)


def __starting_point():
    main()


__starting_point()
