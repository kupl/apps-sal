n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = 10 ** (k - 1)
res = 1
q = 10 ** 9 + 7
for i in range(n // k):
    res1 = (((t * 10) - 1) // a[i] + 1) % q
    z = ((t * b[i]) - 1) // a[i] + 1
    if (b[i] == 0):
        z = 0
    x = (((t * b[i] + t - 1) // a[i])) + 1
    res1 = (res1 - x + z) % q
    res = (res * res1) % q
print(res)
