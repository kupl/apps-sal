s = input()
n = len(s)
a = 0
z = n - 1

for i in range(n):
    if s[i] == "A":
        a = i
        break

for i in range(n):
    if s[i] == "Z":
        z = i

print((z - a + 1))

