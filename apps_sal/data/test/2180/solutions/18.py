n = int(input())
print(n * n // 2 + n % 2)
s1 = ''.join(['C' if x % 2 == 0 else '.' for x in range(n)])
s2 = ''.join(['C' if x % 2 == 1 else '.' for x in range(n)])
for i in range(n):
    print(s1 if i % 2 == 0 else s2)
