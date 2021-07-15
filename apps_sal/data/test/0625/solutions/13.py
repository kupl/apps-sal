n = int(input())
summ = 0
if n % 2 == 0:
    summ = n // 2
else:
    summ = -(n // 2 + 1)
print(summ)

