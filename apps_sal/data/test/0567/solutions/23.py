n = int(input())
line = input()
a = [int(x) for x in line.split()]

result = max([min(x - 1, 1000000 - x) for x in a])

print(result)
