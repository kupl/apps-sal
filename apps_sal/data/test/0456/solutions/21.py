n = int(input())
s = input()
ans = ''
last_ind = 0
i = 0
while i < n:
    if s[i:i + 3] == 'ogo':
        i += 2
    else:
        i += 1
        if i - last_ind > 1:
            ans += '***'
        else:
            ans += s[last_ind:i]
        last_ind = i
print(ans)
