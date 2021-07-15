n = int(input())
k = 0
if n % 7 == 6:
    k = 1
print(2*(n // 7) + k, 2*(n // 7) + min(n % 7, 2))

