A, B = list(map(int, input().split()))
z = (["#"] * 100 + ["\n"]) * 50

for a in range(A - 1):
    j = a % 50
    z[(j * 2) + ((a // 50) % 2) + 202 * (a // 50)] = "."
z2 = (["."] * 100 + ["\n"]) * 50

for a in range(B - 1):
    j = a % 50
    z2[(j * 2) + ((a // 50) % 2) + 101 + 202 * (a // 50)] = "#"
print((100, 100))
print(("".join(z) + "".join(z2)))
