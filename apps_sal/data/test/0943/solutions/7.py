n = int(input())
a = list(map(int, input().split()))

mn = 1000000000000000000000001
if sum(a) % 2 == 0:
    print(sum(a))
else:
    for i in range(n):
        if a[i] % 2 == 1:
            mn = min(mn, a[i])
    print(sum(a)-mn)
