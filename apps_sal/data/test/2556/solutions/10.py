n = int(input())
for i in range(n):
    (count, minSum) = list(map(int, input().split()))
    ost = minSum % count
    r = minSum // count
    ans = r ** 2 * count
    ans -= ost * r ** 2
    ans += (r + 1) ** 2 * ost
    print(ans)
