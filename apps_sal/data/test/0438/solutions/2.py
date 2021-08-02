n = int(input().strip())
k = int(((8 * n + 1) ** 0.5 - 1) // 2)
s = ""

a = []
for i in range(k - 1):
    s += str(i + 1) + " "
s += str(n - (k * (k - 1)) // 2)

print(k)
print(s)
