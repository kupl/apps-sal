x = int(input())
j = sorted([int(i) for i in list(input().split())])
javab = 0
for i in range(x):
    javab += abs(i + 1 - j[i])
print(javab)
