x = int(input())
print((max([pow(i, j) for i in range(1, 32)
           for j in range(2, 10) if pow(i, j) <= x])))

