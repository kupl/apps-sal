for __ in range(int(input())):
    a = input()
    ans = a[0]
    for i in range(1, len(a), 2):
        ans += a[i]
    print(ans)
