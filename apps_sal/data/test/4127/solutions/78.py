(a, b) = map(str, input().split())
a = int(a)
b = list(b)
c = int(b[0]) * 100 + int(b[2]) * 10 + int(b[3])
num = a * c
print(num // 100)
