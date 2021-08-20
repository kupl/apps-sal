N = int(input())
calc = 1
for i in range(1, N + 1):
    calc = i * calc % (10 ** 9 + 7)
print(calc)
