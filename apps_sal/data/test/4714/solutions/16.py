A, B = map(int, input().split())

Numbers = []

for i in range(A, B + 1):
    number = str(A)
    if number[0] == number[4] and number[1] == number[3]:
        Numbers.append(number)
    A += 1

print(len(Numbers))
