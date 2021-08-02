n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
a.sort(reverse=True)
b.sort()
if n % 2:
    a_med = a[n // 2]
    b_med = b[n // 2]
    print(b_med - a_med + 1)
else:
    a_med = (a[n // 2 - 1] + a[n // 2]) / 2
    b_med = (b[n // 2 - 1] + b[n // 2]) / 2
    print(int((b_med - a_med) * 2) + 1)
