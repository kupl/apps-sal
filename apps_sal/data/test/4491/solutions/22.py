N = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
A = []
B = []
suma = 0
sumb = 0
for n in range(N):
    suma += a[n]
    A.append(suma)
for n in reversed(range(N)):
    sumb += b[n]
    B.append(sumb)
MAX = 0
for n in range(N):
    MAX = max(MAX, A[n] + B[N - n - 1])
print(MAX)
