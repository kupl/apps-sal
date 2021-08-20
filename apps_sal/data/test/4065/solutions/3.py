n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(1)
else:
    ans = 1
    num = 1
    for i in range(1, n):
        if a[i] <= 2 * a[i - 1]:
            num += 1
            ans = max(ans, num)
        else:
            num = 1
    ans = max(ans, num)
    print(ans)
