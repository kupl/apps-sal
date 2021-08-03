def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 10 ** 10
    for i in range(n):
        x = i if i > n - i - 1 else n - i - 1
        ans = min(ans, arr[i] // x)
    print(ans)


main()
