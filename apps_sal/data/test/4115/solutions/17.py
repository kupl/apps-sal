s = input()
n = len(s)
cnt = 0
i = 0
j = -1
d = 0
while d != n//2:
    if s[i] != s[j]:
        cnt += 1
    i+=1
    j-=1
    d+=1

print(cnt)
