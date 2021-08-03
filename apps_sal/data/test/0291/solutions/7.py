s = input().split()
a = int(s[0])
b = int(s[1])
p = 0
while True:
    p += 1
    a *= 3
    b *= 2
    if a > b:
        break
print(p)
