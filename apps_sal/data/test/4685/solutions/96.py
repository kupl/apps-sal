a = list(map(int, input().split()))
a.sort()
k = int(input())
res = a[0] + a[1] + a[2] * 2 ** k
print(res)
