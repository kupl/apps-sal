def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    kek = [0] * (n - 1)
    for i in range(n - 1):
        kek[i] = -arr[i + 1] + arr[i]

    kek.sort()

    ans = arr[-1] - arr[0]
    for i in range(k - 1):
        ans += kek[i]

    print(ans)

    return 0


main()
