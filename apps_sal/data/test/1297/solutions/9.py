s = input()
x = 1
c = s[0]
n = 0
for i in range(1, len(s)):
    if s[i] == c:
        x += 1
    else:
        if x % 2 == 0:
            n += 1
        x = 1
        c = s[i]

if x % 2 == 0:
    n += 1

print(n)
