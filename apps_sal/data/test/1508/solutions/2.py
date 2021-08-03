n = int(input())
a = list(map(int, input().split()))
mi = min(a)
ma = max(a)
ans = []
ans.append(ma)
a.sort()
print(ma, *a[1:len(a) - 1], end=' ')
print(mi)
