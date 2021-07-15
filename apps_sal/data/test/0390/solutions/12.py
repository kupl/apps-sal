def main():
    n, c1, c2 = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    ans = 0
    if n % 2 and a[n // 2] == 2:
        ans = min(c1, c2)
    for i in range(n // 2):
        if a[i] == 0 and a[n - 1 - i] == 1 or a[i] == 1 and a[n - 1 - i] == 0:
            print(-1)
            return
        if a[i] == 2 and a[n - 1 - i] == 2:
            ans += 2 * min(c1, c2)
        elif a[i] != 2 and a[n - 1 - i] != 2:
            continue
        elif a[i] == 0 or a[n - 1 - i] == 0:
            ans += c1
        else:
            ans += c2
    print(ans)


main()

