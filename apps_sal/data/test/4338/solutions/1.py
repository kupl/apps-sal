(n, x, y) = map(int, input().split())
a = list(map(int, input().split()))
if y - x >= 0:
    ans = 0
    for elem in a:
        if elem <= x:
            ans += 1
    print((ans + 1) // 2)
else:
    print(n)
