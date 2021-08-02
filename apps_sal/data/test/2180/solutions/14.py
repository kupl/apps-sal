n = int(input())
print(int((n ** 2 + 1) / 2))
for i in range(n):
    str = ''
    for j in range(n):
        str += ('C', '.')[(i + j) % 2 == 1]
    print(str)
