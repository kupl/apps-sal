A, B = map(int, input().split())

mat = []
for i in range(100):
    array = ["."] * 20 + ["#"] * 20
    mat.append(array)

for i in range(B - 1):
    j = 2 * (i // 10)
    k = 2 * (i % 10)
    mat[j][k] = "#"
for i in range(A - 1):
    j = 2 * (i // 10)
    k = 2 * (i % 10) + 21
    mat[j][k] = "."

print(100, 40)
for i in range(100):
    print("".join(mat[i]))
