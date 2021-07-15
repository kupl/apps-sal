sections=int(input())

ones = int(sections / 2)
printSeven = False
if (sections % 2 != 0):
    ones = ones - 1
    printSeven = True

if (printSeven):
    print('7', end='')

print('1' * ones)
