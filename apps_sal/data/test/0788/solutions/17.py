s = input()
s = s[::-1]
f = 0
for i in range(len(s)):
    if s[i] == 'A':
        x = 1
    else:
        x = int(s[i])
        if x == 0:
            x = 9
    f += x
print(f)
