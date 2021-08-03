__author__ = 'User'
a, b = list(map(int, input().split()))
mx = min(a, b)
s = a + b - mx * 2
print(mx, s // 2)
