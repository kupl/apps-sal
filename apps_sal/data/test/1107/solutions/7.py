a=int(input())
s=input()
n=0
for i in range(a,len(s),a):
    if s[i-2]==s[i-1] and s[i-1]==s[i-3] :
        n+=1   
print(n)

