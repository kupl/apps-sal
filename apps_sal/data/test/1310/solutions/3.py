m = int(input())
a = list(map(int, input().split()))

nitest = 0

for i in range(m):
    xor = 0
    for j in range(i, m):
        xor = a[j] ^ xor
        nitest = max(nitest, xor)
print(nitest)
