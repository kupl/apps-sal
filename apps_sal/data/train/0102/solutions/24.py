t = int(input())
for i in range(t):
    r = int(input())
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = 0
    i = 0
    while True:
        if i == 9:
            i = 0
        if a[i] <= r:
            ans += 1
        if a[i] > r:
            break
        a[i] = a[i] * 10 + (a[i] % 10)
        i += 1
    print(ans)
