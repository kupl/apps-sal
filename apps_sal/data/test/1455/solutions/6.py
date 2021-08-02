n = int(input())
a = []
print(n // 2 + 1)
for i in range(n // 2):
    print(i + 1, i + 1)
    print(i + 1, i + 2)
if n % 2 == 1:
    print((n + 1) // 2, (n + 1) // 2)
