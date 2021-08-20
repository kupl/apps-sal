(n, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
minim = 10 ** 18
for i in a:
    if k % i == 0:
        minim = min(minim, k // i)
print(minim)
