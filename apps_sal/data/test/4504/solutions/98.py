s = input()

s = s[::-1]
if len(s) % 2 == 1:
    s = s[1:]
else:
    s = s[2:]

while len(s) >= 2:
    half = len(s) // 2
    if s[:half] == s[half:]:
        print(len(s))
        break
    s = s[2:]
