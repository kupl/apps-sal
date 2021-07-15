n = int(input())
for elem in [523776, 130816, 32640, 8128, 2016, 496, 120, 28, 6, 1]:
    if n % elem == 0:
        print(elem)
        break
