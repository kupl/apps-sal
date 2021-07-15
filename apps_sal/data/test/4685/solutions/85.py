a = list(map(int, input().split()))
k = int(input())

a.sort()

print(sum(a[:-1]) + a[-1] * 2 ** k)
