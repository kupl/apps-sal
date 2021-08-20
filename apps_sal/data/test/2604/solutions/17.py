(r, d) = list(map(int, input().split()))
n = int(input())
counter = 0
for i in range(n):
    (x, y, r_k) = list(map(int, input().split()))
    if (x ** 2 + y ** 2) ** (1.0 / 2.0) - r_k >= r - d and (x ** 2 + y ** 2) ** (1.0 / 2.0) + r_k <= r:
        counter += 1
print(counter)
