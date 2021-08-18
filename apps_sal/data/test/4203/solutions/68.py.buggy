s = input()
count = 0
for i in range(0, len(s)):
    if i == 0 and s[i] == 'A':
        continue
    if i == 1 and 97 <= ord(s[i]) <= 122:
        continue
    if 2 <= i <= len(s) - 2:
        if s[i] == 'C':
            count += 1
            continue
        elif 97 <= ord(s[i]) <= 122:
            continue
    if count == 0 or count >= 2:
        break
    if i == len(s) - 1 and 97 <= ord(s[i]) <= 122:
        print("AC")
        return
print("WA")
