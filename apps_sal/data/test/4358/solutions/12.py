N = int(input())
a = []

for _ in range(0, N):
    a.append(int(input()))

a1 = sorted(a, reverse=True)
price = a1[0] // 2 + sum(a1) - a1[0]

print(price)
