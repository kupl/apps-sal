k, r = list(map(int, input().split()))
e = 1
j = 1
while e > 0:
    e = min((j * k - r) % 10, j * k % 10)
    j += 1
print(j - 1)
