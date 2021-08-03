s = input()
n = len(s)

a = ""

for x in range(n):
    if x % 2 == 0:
        a = a + "1"
    else:
        a = a + "0"

count = 0
for y in range(n):
    if s[y] != a[y]:
        count += 1

print((min(count, n - count)))
