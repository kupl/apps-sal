def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))
    d0 = [0]*n
    d0[n-1] = a[n-1]
    d1 = [0]*n
    d1[n-1] = b[n-1]

    for i in range(n-2, -1, -1):
        d0[i] = max(a[i]+d1[i+1], b[i]+d0[i+1])
        d1[i] = max(b[i]+d1[i+1], c[i]+d0[i+1])
    print(d0[0])


def __starting_point():
    main()

__starting_point()
