def bin_search(a):
    nonlocal prices
    nonlocal n
    l, r = 0, n - 1
    while l < r:
        m = (l + r + 1) // 2
        if prices[m] <= a:
            l = m
        else:
            r = m - 1
    return l


n = int(input())
prices = sorted(list(map(int, input().split())))
q = int(input())
for i in range(q):
    money = int(input())
    ans = bin_search(money)
    print(ans + 1 if money >= prices[0] else 0)

