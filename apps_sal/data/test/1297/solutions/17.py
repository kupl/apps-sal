s = input()
result = 0
last_ch = s[0]
last_ch_len = 1
for i in range(1, len(s)):
    if s[i] == last_ch:
        last_ch_len += 1
    else:
        if last_ch_len % 2 == 0:
            result += 1
        last_ch_len = 1
        last_ch = s[i]
if last_ch_len % 2 == 0:
    result += 1
print(result)
