s = input()
count=0
max_count=0
for i in range(len(s)):
    if(s[i]=="A"or s[i]=="T"or s[i]=="G"or s[i]=="C"):
        count+=1
    else:
        if(max_count<count):
            max_count=count
            count=0
        else:
            count=0
print((max(max_count,count)))

