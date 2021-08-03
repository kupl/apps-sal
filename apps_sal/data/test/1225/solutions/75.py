h = int(input())
c = 0
while h > 0:
    h = h // 2
    c += 1
print(2**c - 1)
