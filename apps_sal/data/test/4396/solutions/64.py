n = int(input())
total = 0
for i in range(n):
    value, currency = input().split()
    if currency == 'JPY':
        total += float(value)
    else:
        total += float(value) * 380000
print(total)
