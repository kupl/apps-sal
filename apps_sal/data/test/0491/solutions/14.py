n = int(input())
if n < 0:
    n = -min(-n // 10, -n // 100 * 10 + -n % 10)
print(n)
