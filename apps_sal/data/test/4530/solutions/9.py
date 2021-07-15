t = int(input())
for q in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    number = 1
    for i in range(0, n - 1):
        if a[i] != a[i + 1]:
            number += 1
    mn = 0
    now = 1
    for i in range(0, n - 1):
        if a[i] == a[i + 1]:
            now += 1
        else:
            mn = max(mn, now)
            now = 1
    mn = max(mn, now)
    print(max(min(number - 1, mn), min(number, mn - 1)))

