primeornot = [True] * (10 ** 5 * 2)
for i in range(2, 10 ** 5):
    if primeornot[i] == True:
        j = 2 * i
        while j < 10 ** 5 * 2:
            primeornot[j] = False
            j += i
x = int(input())
for i in range(x, 10 ** 5 * 2):
    if primeornot[i] == True:
        print(i)
        break
