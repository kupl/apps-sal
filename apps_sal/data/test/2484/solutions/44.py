def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(1)
        return
    ans = n
    l = 0
    now = a[0]
    for r in range(1, n):
        if now & a[r] == 0:
            now = now ^ a[r]
            continue
        now = now ^ a[r]
        for new_l in range(r - 1, l - 1, -1):
            if a[new_l] & a[r] != 0:
                break
        new_l += 1
        for i in range(l, new_l):
            now = now ^ a[i]
        ans += (r - l) * (r - l - 1) // 2 - (r - new_l) * (r - new_l - 1) // 2
        l = new_l
    r += 1
    ans += (r - l) * (r - l - 1) // 2
    print(ans)


main()
