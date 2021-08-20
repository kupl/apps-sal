n = int(input())
s = input()
while True:
    used = False
    for i in range(1, len(s)):
        if s[i - 1] + s[i] == 'UR' or s[i - 1] + s[i] == 'RU':
            s = s[:i - 1] + 'D' + s[i + 1:]
            used = True
            break
    if not used:
        break
print(len(s))
