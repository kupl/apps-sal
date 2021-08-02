Count = [2, 7, 2, 3, 3, 4, 2, 5, 1, 2]
print((lambda x: Count[x[0]] * Count[x[1]])(list(map(int, list(input())))))
