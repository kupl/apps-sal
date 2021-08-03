n = int(input())
A = list(map(int, input().split()))
paA = [0 for _ in range(n - 1)]
paA[0] = A[n - 1]
mod = 10**9 + 7
for i in range(1, n - 1):
    paA[i] = paA[i - 1] + A[n - 1 - i]
suma = 0
for i in range(n - 1):
    suma += A[i] * paA[n - i - 2]
    suma = suma % mod
print(suma)
