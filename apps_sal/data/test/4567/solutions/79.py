n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
s.sort()

if sum(s)%10==0:
    for i in range(n):
        if s[i]%10!=0:
            print((sum(s)-s[i]))
            return
    print((0))
    return
print((sum(s)))

