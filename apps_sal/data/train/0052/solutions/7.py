I = input
n = int(I())
R = list(range(n))
a = sorted(int(I())for _ in R)
k = 0
for i in R:
    k = (k + a[i] * a[n - i - 1]) % 10007
print(k)
