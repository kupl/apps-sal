n = int(input())
l1 = []
l1.append(1)
l1.append((n * (n + 1)) // 2)
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        x = (n // i) * (2 + ((n // i) - 1) * i) // 2
        if x not in l1:
            l1.append(x)
    k = n // i
    if n % k == 0:
        x = (n // k) * (2 + ((n // k) - 1) * k) // 2
        if x not in l1:
            l1.append(x)
l1.sort()
for item in l1:
    print(item, end=" ")
