boys, girls = input().split()

boys = int(boys)
girls = int(girls)

print(boys + girls - 1)

for i in range(1, girls + 1):
    print(1, i)

for i in range(2, boys + 1):
    print(i, girls)
