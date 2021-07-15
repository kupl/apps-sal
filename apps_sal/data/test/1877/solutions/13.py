n = int(input())

s = input()

x = 0
y = 0

k = 0
for i in range(len(s) - 1):
    if s[i] == 'U':
        y += 1
    else:
        x += 1
    if x == y:
        if s[i] == s[i + 1]:
            k += 1

print(k)

