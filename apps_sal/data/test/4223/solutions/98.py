n = int(input())
s = list(input())
cnt = 1
for i in range(n-1):
    if s[i]!=s[i+1]:
        cnt += 1
print(cnt)
