n = int(input())
s = input()
ans = ''
i = 0
while i < len(s):
    if i <= len(s) - 3 and s[i:i + 3] == 'ogo':
        j = i + 3
        while s[j:j + 2] == 'go':
            j += 2
        ans += '***'
        i = j - 1
    else:
        ans += s[i]
    i += 1
print(ans)
