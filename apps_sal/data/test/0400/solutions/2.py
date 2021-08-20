(n, k) = list(map(int, str.split(input())))
a = sorted(map(int, str.split(input())), key=lambda x: x % 10, reverse=True)
rating = 0
for i in range(n):
    delta = 10 - a[i] % 10
    if k >= delta and a[i] < 100:
        a[i] += delta
        k -= delta
    rating += a[i] // 10
for i in range(n):
    if k < 10:
        break
    while a[i] < 100 and k >= 10:
        a[i] += 10
        k -= 10
        rating += 1
print(rating)
