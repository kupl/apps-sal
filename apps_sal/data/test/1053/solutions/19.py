n = int(input()) - 1; a = 0
for i in range(40):
    k = 1 << i; a += (n + k) // (k << 1) * k
print(a)
