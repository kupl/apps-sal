def main():
    n, m = list(map(int, input().split()))
    st = input()
    a = [0] * n
    for i in range(n):
        a[i] = ord(st[i]) - 96
    a.sort()
    ans = 0
    last = -1
    c = 0
    for i in range(n):
        if a[i] - last >= 2:
            c += 1
            last = a[i]
            ans += a[i]
        if c == m:
            print(ans)
            return
    print(-1)
main()

