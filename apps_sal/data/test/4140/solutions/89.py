s = list(str(input()))
cnt = 0

if len(s)>1 and s[0]==s[1]:
    if s[0] == '1':
        s[1] = '0'
    else:
        s[1] = '1'
    cnt += 1

for i in range(1,len(s)-1):
    if s[i] == s[i+1]:
        s[i+1] = s[i-1]
        cnt += 1

print(cnt)

