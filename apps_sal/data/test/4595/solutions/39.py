s = input()
a_number = 0
z_number = 0

for i in range(len(s)):
    if s[i] == 'A':
        a_number = i
        break

for j in reversed(range(len(s))):
    if s[j] == 'Z':
        z_number = j
        break

print(z_number - a_number + 1)
