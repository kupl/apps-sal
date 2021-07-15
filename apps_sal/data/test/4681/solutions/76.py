n = int(input())
list_lucas = [2, 1]
lucas = 0
for i in range(0, n - 1):
    lucas = list_lucas[i] + list_lucas[i + 1]
    list_lucas.append(lucas)
    lucas = 0
print(list_lucas[-1])
