n = int(input())
s = sum([int(x) for x in str(n)])
while s % 4 != 0:
    n += 1
    s = sum([int(x) for x in str(n)])
print(n)
