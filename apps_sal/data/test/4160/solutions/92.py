
X = int(input())

i = 0
a = 100
while a < X:
    a += a // 100
    i += 1

print(i)
