a = input()
summ = 0
lena = len(a)
for i in range(1, lena):
    summ += 10 ** (i - 1) * 9 * i
summ += lena * (int(a) - 10 ** (lena - 1) + 1)
print(summ)


