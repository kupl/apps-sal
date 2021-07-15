s = input()
for i in range(len(s)):
    if s[i] == s[i-1] and i-1>=0:
        print(i-1+1, i+1)
        return
    elif (i+1)<=len(s)-1 and s[i+1] == s[i]:
        print(i+1, i+1+1)
        return
    elif (i-1)>=0 and (i+1)<= len(s)-1 and s[i-1]==s[i+1]:
        print(i-1+1,i+1+1)
        return
print(-1, -1)
