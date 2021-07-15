s = input()

a = 0
i = 0

while i < len(s)/2:
    if s[i] != s[-i-1]:
        a += 1
    i += 1

print(a)

