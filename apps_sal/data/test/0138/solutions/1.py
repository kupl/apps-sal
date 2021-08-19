(n, a, b, c) = list(map(int, input().split()))
a = [0, a, b, c]
for _ in range(100):
    for i in range(4):
        for j in range(4):
            to = (i + j) % 4
            if a[to] > a[i] + a[j]:
                a[to] = a[i] + a[j]
print(a[(4 - n % 4) % 4])
