ansl1 = list("#" * (100 * 25))
ansl2 = list("." * (100 * 25))

a, b = map(int, input().split())

for i in range(a - 1):
    ansl1[2 * i] = "."

for i in range(b - 1):
    ansl2[2 * i] = "#"
print(100, 100)

for i in range(25):
    print("".join(ansl1[(i * 100):(i * 100) + 100]))
    print("#" * 100)

for j in range(24, -1, -1):
    print("".join(ansl2[(j * 100):(j * 100) + 100]))
    print("." * 100)
