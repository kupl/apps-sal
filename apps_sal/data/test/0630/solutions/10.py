def main():
    n, k = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [0] * n
    for i in range(n):
        l, r = 0, n - 1
        a[i] = 0
        if b[i]:
            l = b[i] + k
            a[i] += a[b[i] - 1]
        l = max(l, i - k)
        r = min(r, i + k)
        if r >= l:
            a[i] += r - l + 1

    print(' '.join(map(str, a)))


main()
