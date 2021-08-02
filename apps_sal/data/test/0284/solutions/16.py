n = int(input())
sol = False
for i in range(max(n // 1234567 + 1, 1)):
    n2 = n - i * 1234567
    for j in range(max(n2 // 123456 + 1, 1)):
        n3 = n2 - j * 123456
        if n3 % 1234 == 0:
            sol = True
            break

print(["NO", "YES"][sol])
