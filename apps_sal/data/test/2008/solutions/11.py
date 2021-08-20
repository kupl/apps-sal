def main():
    n = int(input())
    arr = []
    for i in range(n):
        (x, y) = map(int, input().split())
        arr.append((x, y))
    ans = 0
    arr.sort(key=lambda a: a[1] - a[0])
    for i in range(n):
        (x, y) = arr[i]
        ans += x * i + (n - 1 - i) * y
    print(ans)
    return 0


main()
