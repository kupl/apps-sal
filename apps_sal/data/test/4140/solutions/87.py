s = input()
cnt = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            cnt += 1
    elif s[i] == '1':
        cnt += 1
print(min(cnt, len(s) - cnt))
