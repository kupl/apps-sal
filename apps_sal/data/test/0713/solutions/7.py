a, b = (int(x) for x in input().split())
print(min(a, b) + 1)
for i in range(min(a, b) + 1):
    print(a - i, i)
