s = input()
cnt = 0
for i in range(len(s)):
    cnt = cnt+1 if s[i] == '+' else cnt-1
print(cnt)
