n = int(input())
s = input()
maxnum = 0
cnt = 0
for i in range(len(s)):
    if s[i] == 'I':
        cnt += 1
        if cnt >= maxnum:
            maxnum = cnt
    elif s[i] == 'D':
        cnt -= 1
print(maxnum)
