def main():
    mod = 10 ** 9 + 7
    pws = [None for i in range(4 * 10 ** 5)]
    pws[0] = 1
    for i in range(1, 4 * 10 ** 5):
        pws[i] = 2 * pws[i - 1] % mod
    n = int(input())
    seq = list(map(int, input().split()))
    seq.sort()
    ans = 0
    for i in range(n):
        ans += seq[i] * (pws[i] - 1)
        ans -= seq[i] * (pws[n - i - 1] - 1)
        ans = ans % mod
    print(ans)


main()
