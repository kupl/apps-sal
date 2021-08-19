import bisect
x = int(input())
a = 2
b = 2
k = {1}
while a <= 31:
    while pow(a, b) <= 1000:
        k.add(pow(a, b))
        b += 1
    b = 2
    a += 1
kl = list(k)
kl.sort()
print(kl[bisect.bisect_right(kl, x) - 1])
