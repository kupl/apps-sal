n = int(input())
s = input()
while s.count('ogo') > 0:
    i = 0
    j = 0
    while s[i:i + 3] != 'ogo':
        i += 1
    if s[i:i + 3] == 'ogo':
        j = i + 3
        while j + 2 <= len(s) and s[j:j + 2] == 'go':
            j += 2
        s = s[:i] + '***' + s[j:]
print(s)
