numbers = []
highest = 0
for _ in range(int(input())):
    numbers.append(int(input()))
    if highest < sum(numbers) / len(numbers):
        highest = sum(numbers) / len(numbers)
print(highest)

"""
FOO = sum(input)
BAR = number input
BAZ = 0
QUZ = 0
	BIGGR OF (
		(PRODUKT OF FOO AN QUZ) 
		AN (PRODUKT OF BAR BAZ)
	) 
	AN (PRODUKT OF FOO AN QUZ))"""
