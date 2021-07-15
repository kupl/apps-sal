k=int(input())
s='codeforces'
a=[1]*10
ans=1
pointer=0
while ans<k:
    ans=ans//a[pointer]
    a[pointer]+=1
    ans=ans*a[pointer]
    pointer=(pointer+1)%10
ans1=[]
for i in range(10):
    for j in range(a[i]):
        ans1.append(s[i])
print(''.join(ans1))

