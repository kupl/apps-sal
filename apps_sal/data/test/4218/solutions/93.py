n = int(input())
if n % 2 == 0:
    odd_count = n // 2
else:
    odd_count = n // 2 + 1
print(odd_count / n)
