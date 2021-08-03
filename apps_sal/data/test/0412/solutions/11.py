n = int(input())
a = list(map(int, input().split()))
r = 2
k = 0
r1 = 1
k1 = 0
t = True
while t:
    for i in range(n):
        if a[i] % r1 == 0:
            k1 += 1
    if k1 != 0:
        k = k1
        k1 = 0
        r = r1
        r1 *= 2
        t = True
    else:
        break
print(r, k)
