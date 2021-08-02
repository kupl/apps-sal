
n, k, x = map(int, input().split())
*Arr, = map(int, input().split())

Prfx = [0] * (n + 2)
Sffx = [0] * (n + 2)

for i in range(0, n):
    Prfx[i + 1] = Prfx[i] | Arr[i]
    Sffx[n - i - 1] = Sffx[n - i] | Arr[n - i - 1]
now = x**k
Res = 0
for i in range(0, n):
    Res = max(Prfx[i] | (Arr[i] * now) | Sffx[i + 1], Res);
print(Res)
