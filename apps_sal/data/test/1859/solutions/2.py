n = int(input())
if n % 2 == 0:
    print(n // 2)
    return

for x in range(2, int(n**0.5 + 1)):
    if n % x == 0:
        print(1 + (n - x) // 2)
        return
print(1)
