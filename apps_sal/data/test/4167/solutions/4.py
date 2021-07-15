n, k = list(map(int, input().split()))

s = 0

if k % 2 == 1:
    s = (n // k) ** 3
else:
    s = (n // k) ** 3 + ((n // (k // 2)) - (n // k)) ** 3

print(s)
