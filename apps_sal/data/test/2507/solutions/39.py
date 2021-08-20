def main():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort()
    F.sort(reverse=True)
    r = A[-1] * F[0]
    l = -1
    while r - l > 1:
        tmp = (l + r) // 2
        k = 0
        for (x, y) in zip(A, F):
            if x * y > tmp:
                k += x - tmp // y
        if K >= k:
            r = tmp
        else:
            l = tmp
    print(r)


main()
