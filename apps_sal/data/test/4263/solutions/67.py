words = ['A','G','C','T']
s = input()
ans = 0
cnt = 0
for i in range(len(s)):
    if s[i] in words:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)
