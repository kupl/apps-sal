n = int(input())
c = str(input())
a = c.count('R')
b = c[:a].count('R')
print(a - b)
