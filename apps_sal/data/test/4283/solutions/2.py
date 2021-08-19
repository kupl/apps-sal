def main():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    a = 0
    b = 0
    while b < n:
        if arr[b] - arr[a] <= 5:
            ans = max(ans, b - a + 1)
            b += 1
        else:
            a += 1
    print(ans)


main()
