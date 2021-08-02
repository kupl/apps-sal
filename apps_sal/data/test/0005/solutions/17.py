def main():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if l <= pos <= r:
        if l == 1:
            if r == n:
                print(0)
                return
            ans += r - pos + 1
            print(ans)
            return
        if r == n:
            ans = pos - l + 1
            print(ans)
            return
        ans = min(pos - l, r - pos) + r - l + 2
        print(ans)
        return
    if pos > r:
        ans += pos - r + 1
        if l > 1:
            ans += r - l + 1
        print(ans)
        return
    ans += l - pos + 1
    if r < n:
        ans += r - l + 1
    print(ans)
    return


main()
