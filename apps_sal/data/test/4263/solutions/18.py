s=input()
ma,cnt=0,0
for i in range(len(s)):
    if s[i] in ["A","C","G","T"]:
        cnt+=1
        ma=max(ma,cnt)
    else:
        cnt=0
print(ma)
