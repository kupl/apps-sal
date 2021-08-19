a = list(map(int, input().split()))
a = sorted(a, reverse=True)
res = a[0] * 10 + a[1] + a[2]
print(res)
