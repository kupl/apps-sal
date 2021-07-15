n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
s = sum(a)
mn, mx = min(a), max(a)
mx_k = mx + m
m -= mx * n - s
if m > 0:
    mx += m // n
    mx += 1 if m % n else 0
print(mx, mx_k)

