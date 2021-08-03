def main():
    n, k = map(int, input().split())
    if k > (n // 2):
        k = n // 2
    ans = 0
    for i in range(k):
        ans += 2 * (n - 2 * i - 2) + 1
    print(ans)


main()
