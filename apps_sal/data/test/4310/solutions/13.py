a = list(map(int, input().split()))
a.sort()
ans = 0 if len(set(a)) == 1 else a[2] - a[0]
print(ans)
