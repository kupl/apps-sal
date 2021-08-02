n = int(input())
rows = [(["C", "."] * (n // 2) + ["C"] * (n % 2)), ([".", "C"] * (n // 2) + ["."] * (n % 2))]
print((n ** 2) // 2 + n % 2)
for i in range(0, n):
    print("".join(rows[i % 2]))
