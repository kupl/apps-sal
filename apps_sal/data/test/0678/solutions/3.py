numbers = []
highest = 0
for _ in range(int(input())):
    numbers.append(int(input()))
    if highest < sum(numbers) / len(numbers):
        highest = sum(numbers) / len(numbers)
print(highest)
'\nFOO = sum(input)\nBAR = number input\nBAZ = 0\nQUZ = 0\n#BOTH SAEM ( \n\tBIGGR OF (\n\t\t(PRODUKT OF FOO AN QUZ) \n\t\tAN (PRODUKT OF BAR BAZ)\n\t) \n\tAN (PRODUKT OF FOO AN QUZ))'
