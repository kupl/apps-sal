n = int(input())
k = 1
t = 1
maxt = 1
while t <= n:
    k += 1
    t = (2 ** k - 1) * 2 ** (k - 1)
    if n % t == 0:
        maxt = t
print(maxt)
