n=input()
#s=n[:(len(n)-1)//2+1]
c=len(n)//2
for i in range(c-1):
    if n[len(n)-c-1-i:]==n[:c+1+i]:
        print('YES')
        print(n[:c+i+1])
        break
else: print('NO')

