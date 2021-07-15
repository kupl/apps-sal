s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i+1] != s[i]:
        cnt += 1
print(cnt)
