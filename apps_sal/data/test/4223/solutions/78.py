n=int(input())
s=input()
t=1
for i in range(1,n):
    if s[i]!=s[i-1]:
        t+=1
print(t)
