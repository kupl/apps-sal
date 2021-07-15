N=int(input())
C=input()

n=0
c=0
for i in range(N)[::-1]:
    if C[i]=="R":
        while n<i:
            if C[n]=="W":
                c+=1
                n+=1
                break
            n+=1
print(c)

