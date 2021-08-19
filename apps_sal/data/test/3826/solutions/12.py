def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = n
    for l in range(0, n + 1):
        s = set(a[:l])
        if len(s) < l:
            break
        r = n - 1
        while r >= l and a[r] not in s:
            s.add(a[r])
            r -= 1
        ans = min(ans, r - l + 1)
    print(ans)


main()
