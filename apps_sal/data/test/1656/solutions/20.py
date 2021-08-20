s = input().split()[0]
wos = []
sum_w = 0
sum_o = 0
for i in range(len(s)):
    if s[i] == 'o':
        wos.append(sum_w + (0 if len(wos) == 0 else wos[-1]))
        sum_o += 1
    elif s[i] == 'v':
        wos.append(0 if len(wos) == 0 else wos[-1])
        if i == 0 or s[i - 1] != 'v':
            pass
        else:
            sum_w += 1
answer = 0
for i in range(len(s)):
    if s[i] == 'o':
        pass
    elif s[i] == 'v':
        if i == 0 or s[i - 1] != 'v':
            pass
        else:
            answer += wos[i]
print(answer)
