n = int(input())
a = [int(z) for z in input().split()]
b = [int(z) for z in input().split()]
shit = set(a + b)
counter = 0
for i in range(n):
    for j in range(n):
        if a[i] ^ b[j] in shit:
            counter += 1
if counter % 2 == 0:
    print("Karen")
else:
    print("Koyomi")
