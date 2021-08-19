T = int(input())
for kase in range(T):
    (a, b) = [int(x) for x in input().split()]
    x = 9
    ans = 0
    while x <= b:
        ans += 1
        x = x * 10 + 9
    print(ans * a)
