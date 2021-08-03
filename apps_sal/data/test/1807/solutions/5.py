def main():
    a, b = map(int, input().split())
    arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    ans = 0
    for i in range(a, b + 1):
        x = i
        while x != 0:
            ans += arr[x % 10]
            x //= 10
    print(ans)


main()
