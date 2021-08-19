n = int(input())
f = input()
a = 0
for i in range(len(f)):
    if f[i] != ' ':
        a += int(f[i])
c = 0
for i in range(1, 6, 1):
    x = a + i - 1
    if x % (n + 1) != 0:
        c += 1
print(c)
