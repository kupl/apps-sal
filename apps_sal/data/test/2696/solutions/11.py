n = int(input())
a = list(map(int, input().split()))

if a[-1] == a[-2]:
    k = n - 1
    while a[k - 1] == a[k] and k >= 1:
        k -= 1
    print(k + 1)
else:
    print(n)
