import sys

s = str(input())

cnt = 0
ans = [0] * len(s)

for i in range(len(s)):
    if(s[i] == '('):
        cnt += 1
    else:
        cnt -= 1
    if(s[i] == '#'):
        ans[i] = 1
    if(cnt < 0):
        print(-1)
        return

i = len(s) - 1

while(s[i] != '#'):
    i -= 1

ans[i] = cnt + 1
cnt = 0

for i in range(len(s)):
    if(s[i] == '('):
        cnt += 1
    elif(s[i] == ')'):
        cnt -= 1
    else:
        cnt -= ans[i]

    if(cnt < 0):
        print(-1)
        return

for i in range(len(s)):
    if(s[i] == '#'):
        print(ans[i])
