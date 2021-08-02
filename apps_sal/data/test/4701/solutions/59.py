n, k = [int(input()) for i in range(2)]
a = 1
for i in range(n):
    if a * 2 > a + k:
        a += k
    else:
        a *= 2
print(a)
