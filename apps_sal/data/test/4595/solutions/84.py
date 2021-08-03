s = input()

for i in range(len(s)):
    if s[i] == 'A':
        start = i
        break

for i in range(1, len(s) + 1):
    if s[(-1) * i] == 'Z':
        end = i
        break

print(len(s) - end - start + 1)
