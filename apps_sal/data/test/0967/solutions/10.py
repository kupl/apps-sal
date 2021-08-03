n = int(input(""))
a = [int(x) for x in input("").split(' ')]
output = 0
cache = 0
for x in range(n - 1):
    if a[x] > a[x + 1]:
        output += 1 + cache
        cache = 0
    else:
        cache += 1
print(output)
