n, z, w = map(int, input().split())
a = list(map(int, input().split()))
print(abs(w - a[0])if n == 1else max(abs(w - a[-1]), abs(a[-1] - a[-2])))
