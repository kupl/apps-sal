s=input()
d=s[0]
a=[ 'a', 'e', 'i', 'o' , 'u']
i=1
while i<len(s)-1:
    d+=s[i]
    if (not(s[i] in a))&(not(s[i+1] in a))&(not(s[i-1] in a))&(not(s[i]==s[i+1]==s[i-1])):
        d+=' '+s[i+1]
        i+=1
    i+=1
if i<len(s):
    d+=s[i]
print(d)

