def chk(a, q, n):
    l = a[0]
    m = a[n - 1]
    if q >= l and q <= m:
        return 'Yes'
    return 'No'


def main():
    (n, q) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    while q > 0:
        q -= 1
        ques = int(input())
        print(chk(A, ques, n))


def __starting_point():
    main()


__starting_point()
