s = list(input())
count = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        if s[i] == '1':
            s[i] = '0'
        else:
            s[i] = '1'
print(count)
