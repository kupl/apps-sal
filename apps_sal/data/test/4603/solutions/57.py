A = int(input())
B = int(input())
C = int(input())
D = int(input())

train_plice = min(A,B)
bus_plice = min(C,D)

min_plice = train_plice + bus_plice
print(min_plice)
