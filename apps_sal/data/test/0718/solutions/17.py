a = int(input())
b = a + 1
while str(b).count('8') == 0:
    b += 1
print(b - a)

