n = int(input())
a = list(map(int, input().split()))

a.sort()

print(a[-1] - sum(a[:-1]) + 1)
