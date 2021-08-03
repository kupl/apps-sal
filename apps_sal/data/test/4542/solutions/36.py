s = input()
counter = 0

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        counter += 1

print(counter)
