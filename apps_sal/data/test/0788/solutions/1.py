s = input()
ans = 1
skip = 0
for i in range(1, 7):
    if skip:
        skip = 0
        continue
    if i + 1 < 7 and s[i] == '1' and (s[i + 1] == '0'):
        ans += 10
        skip = 1
    else:
        ans += ord(s[i]) - ord('0')
print(ans)
