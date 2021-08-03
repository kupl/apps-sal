def main():
    n = int(input())
    mod = 998244353
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    for i in range(n):
        a[i] *= (i + 1) * (n - i)
    a.sort(reverse=1)
    ans = 0
    for i in range(n):
        ans = (ans + a[i] * b[i]) % mod
    print(ans)

    return 0


main()
