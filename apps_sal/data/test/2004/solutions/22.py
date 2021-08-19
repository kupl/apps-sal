from sys import stdin, stdout
n = int(stdin.readline().rstrip())
if n % 2 == 0:
    print(3 * (n // 2))
else:
    print(3 * (n - 1) // 2 + 1)
bombOrder = []
i = 2
while i <= n:
    bombOrder.append(str(i))
    i += 2
i = 1
while i <= n:
    bombOrder.append(str(i))
    i += 2
i = 2
while i <= n:
    bombOrder.append(str(i))
    i += 2
print(' '.join(bombOrder))
