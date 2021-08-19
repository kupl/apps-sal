(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
chet_a = 0
nech_a = 0
chet_b = 0
nech_b = 0
for i in range(n):
    if a[i] % 2 == 0:
        chet_a += 1
    else:
        nech_a += 1
for i in range(m):
    if b[i] % 2 == 0:
        chet_b += 1
    else:
        nech_b += 1
print(min(chet_a, nech_b) + min(nech_a, chet_b))
