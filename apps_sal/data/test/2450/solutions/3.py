def solv():
    (x, y, on, tw) = map(int, input().split())
    ans = 0
    for n in range(x):
        s = input()
        tot = 0
        for n in s:
            if n == '.':
                tot += 1
            else:
                a = tot * on
                b = tot // 2 * tw + tot % 2 * on
                ans += min(a, b)
                tot = 0
        a = tot * on
        b = tot // 2 * tw + tot % 2 * on
        ans += min(a, b)
    print(ans)


for n in range(int(input())):
    solv()
