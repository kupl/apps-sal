s = input()
cnt = 0
cur = s[0]
strk = 1

for i in range(1, len(s)):
    if s[i] == cur:
        strk += 1
    else:
        cnt += 1
        cur = s[i]
        strk = 1

cnt += 1

print(cnt-1)
