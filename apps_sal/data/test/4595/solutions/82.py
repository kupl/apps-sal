s = input()

max_len = 0
past = -1
for i in range(len(s)):
    if s[i] == 'A' and past == -1:
        past = i
        continue
    if s[i] == 'Z':
        max_len = max(max_len, i - past + 1)

print(max_len)
