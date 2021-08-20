(A, B, K) = map(int, input().split())
lst = []


def divisor(n, m):
    if n > m:
        (n, m) = (m, n)
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            lst.append(i)
    lst.reverse()
    print(lst[K - 1])


divisor(A, B)
