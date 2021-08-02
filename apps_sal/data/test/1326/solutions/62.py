N = int(input())
suma = 0
for i in range(1, N + 1):
    a = N // i
    suma += i * (a * (a + 1)) // 2
print(suma)
