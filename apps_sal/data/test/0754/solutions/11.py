n = int(input())
s=input()
count=0
j=0
i=1
while i<n:
    if s[i]==s[j]:
        count+=1
    else:
        j=i
    i+=1
print(count)
