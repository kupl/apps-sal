n=int(input())
s=list(input())
for i in range(len(s)-1,0,-1):
    if s[i]==s[i-1]:
        s.pop(i)
print((len(s)))

