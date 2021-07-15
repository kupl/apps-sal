n, m = map(int, input().split())
asd = 10 ** 9
for i in range(n):
    a, b = map(int, input().split())
    if a / b < asd:
        asd = a / b
print(asd * m)
