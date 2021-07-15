n, k = map(int, input().split())
a = []
for i in range(1, k):
    if n % i == 0:
        g = n // i
        a.append(g * k + i)
print(min(a))
