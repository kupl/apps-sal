(a, b) = map(int, input().split())
z = 0
while a < b:
    if b % 2 == True:
        z += 1
        b += 1
    else:
        b = b // 2
        z += 1
print(str(int(abs(z + a - b))))
