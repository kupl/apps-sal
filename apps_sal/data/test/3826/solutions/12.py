def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = n
    for l in range(0, n + 1):
        s = set(a[:l])
        if len(s) < l:
            break

        # print(l, s)

        r = n - 1
        while r >= l and a[r] not in s:
            s.add(a[r])
            r -= 1

        # print(r, s)
        ans = min(ans, r - l + 1)
        # print()

    print(ans)


main()
