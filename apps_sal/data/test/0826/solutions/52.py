n = int(input())
right = 0
left = 10 ** 18
while abs(right - left) > 1:
    k = (right + left) // 2
    if k * (k + 1) <= (n + 1) * 2:
        right = k
    else:
        left = k
print(n - right + 1)
