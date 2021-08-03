h, n = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    h = h - a[i]
if h <= 0:
    print("Yes")
else:
    print("No")
