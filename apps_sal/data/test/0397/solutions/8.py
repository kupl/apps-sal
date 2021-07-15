n, k = list(map(int, input().split()))
c = n + k
p = int(0.5 * ((8 * c + 9) ** 0.5 - 3))
print(n - p)

