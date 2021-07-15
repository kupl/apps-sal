n = int(input())
s = input()
i = 0
ans = ''
while i < n:
    if i <= n - 3 and s[i:i + 3] == 'ogo':
        j = i + 3
        while j < n - 1:
            if s[j] == 'g' and s[j + 1] == 'o':
                j += 2
            else:
                break
        ans += '***'
        i = j
    else:
        ans += s[i]
        i += 1
print(ans)

