n = int(input())
s = input()
x = 0
y = 1
for i in range (n - 1):
    if s[i] == s[i + 1]:
        x += 1
    if s[i] != s[i + 1]:
        y += 1
print(y + min(2, x))

