s = [c for c in input()]
current_char = 97
for i in range(len(s)):
    if current_char == 123:
        continue
    elif ord(s[i]) <= current_char:
        s[i] = chr(current_char)
        current_char += 1
if current_char < 123:
    print(-1)
else:
    print(''.join(s))
