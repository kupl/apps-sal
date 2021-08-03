n = int(input())
s = input()
p = ''
for i in range(n - 1):
    if s[i] > s[i + 1]:
        p = s[:i] + s[i + 1:]
        break
    if i == n - 2:
        p = s[:-1]
print(p)
