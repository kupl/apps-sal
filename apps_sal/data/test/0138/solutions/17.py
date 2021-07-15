n, a, b, c = map(int, input().split())
mn = 10 ** 12
arr = [0, a, b, c]
for i in range(30):
    for j in range(30):
        q = (4 - (n % 4 + i * 3 + j * 2) % 4) % 4
        mn = min(mn, arr[3] * i + arr[2] * j + arr[1] * q)
print(mn)
