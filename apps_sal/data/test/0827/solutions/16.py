n=int(input())
t=input()
s="110"*(10**5)
c=0
for i in range(3):
    if s[i:i+n]==t:
        c+=10**10-(n+i-1)//3
print(c)
