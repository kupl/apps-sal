s = input()
n = len(s)
c = 0
for i in range(n):
    if int(s[i]) % 2 == i % 2:
        c += 1
print(min(c, n - c))
