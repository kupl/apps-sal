a = 0; n = int(input()) - 1
for i in range(40):
    k = 1 << i; a += (n + k) // (k * 2) * k
print(a)
