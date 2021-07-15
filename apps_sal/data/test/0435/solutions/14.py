
n,k=list(map(int,input().split()))


s=input()

a=0
b=0
p=0
ind=0

for i in range(n):

    if s[i] == 'a':
        a += 1
    else:
        b += 1

    if min(a, b) > k:
        if s[p] == 'a':
            a -= 1

        else:
            b-=1

        p += 1


    else:
        ind+=1


























print(ind)


                      
            


