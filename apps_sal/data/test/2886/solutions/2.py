s = input()

n = len(s)

for i in range(n - 1):
    if s[i] == s[i + 1]:
        print((i + 1, i + 2))
        return

for i in range(n - 2):
    if s[i] == s[i + 2]:
        print((i + 1, i + 3))
        return

print((-1, -1))

