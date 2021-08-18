s = input()
n = len(s)
for i in range(1, n):
    if s[i] == s[i - 1]:
        print(i, i + 1)
        return

for i in range(2, n):
    if s[i] == s[i - 2]:
        print(i - 1, i + 1)
        return

print(-1, -1)
