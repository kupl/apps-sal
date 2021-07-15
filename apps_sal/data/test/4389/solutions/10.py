t=int(input())
count=0
while count<t:
    count+=1
    s=input()
    ans=''
    i=0
    while i<len(s):
        ans+=s[i]
        i+=2
    print(ans+s[-1])

