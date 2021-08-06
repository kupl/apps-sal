n = int(input())
a = list(map(int, input().split()))
a.sort()
if n % 2 == 0:
    print((sum(a) - sum(a[:n // 2])) * 2 - max(a))
else:
    print((sum(a) - sum(a[:n // 2])) * 2 - max(a) - a[n // 2])
