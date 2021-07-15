n, k = [int(i) for i in input().split()]
kol2 = 0
kol5 = 0
n1 = n
while (n1 % 5 == 0):
    n1 /= 5
    kol5 += 1
n1 = n
while (n1 % 2 == 0):
    n1 /= 2
    kol2 += 1
while (k - kol2 > 0):
    n *= 2
    kol2 += 1
while (k - kol5 > 0):
    n *= 5
    kol5 += 1
print(n)
