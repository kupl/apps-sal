n = int(input())
x = []
u = []
yen = 0
bit = 0
for i in range(n):
    a, b = input().split()
    x.append(float(a))
    u.append(b)
for i in range(n):
    if u[i] == "JPY":
        yen += x[i]
    else:
        bit += x[i]
print(yen + 380000 * bit)
