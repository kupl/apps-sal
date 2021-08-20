(n, w) = map(int, input().split())
n *= 2
arr = list(map(int, input().split()))
arr.sort()
g = arr[:n // 2]
b = arr[n // 2:]
first_g = g[0]
first_b = b[0]
if first_g * 2 > first_b:
    first_g = first_b / 2
elif first_g * 2 < first_b:
    first_b = first_g * 2
ans = first_g * n / 2 + first_b * n / 2
print(min(ans, w))
