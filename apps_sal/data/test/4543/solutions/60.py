a, b = map(str, input().split())
c = int(a + b)

for i in range(int(c ** 0.5), int(c ** 0.5) + 1):
    if i ** 2 == c:
        print('Yes')
        return

print('No')
