for _ in range(int(input())):
    a = input()
    ans = ''
    ans += a[0] + a[1]
    for i in range(3, len(a), 2):
        ans += a[i]
    print(ans)
