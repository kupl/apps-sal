n = int(input())
m = n // 2
if n % 2 == 1:
    print(m * (m + 1))
elif n % 2 == 0:
    print(m ** 2)
