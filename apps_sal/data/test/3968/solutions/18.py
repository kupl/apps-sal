
input()
a = sorted(map(int, input().split()))[::-1]
a[1:1] = a.pop(),
print(*a)
