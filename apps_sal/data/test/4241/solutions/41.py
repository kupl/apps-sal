s = input()
t = input()
ans=10**4
for a in range(len(s)-len(t)+1):
    tmp=0
    for b in range(len(t)):
        if s[a+b] == t[b]:
            tmp+=1
    ans=(min(ans, len(t)-tmp))
print(ans)
