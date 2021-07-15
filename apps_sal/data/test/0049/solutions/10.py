import sys
k=int(input())
if type(k)!=int or k<=0 or k>pow(10,12) :
        print("wrong input. try again")
        return
lim_init=lim=decimal=9
c=0
while True:
        c+=1
        if k<=lim:
                diff=lim-k #189-21
                pos=diff%c
                diff=int(diff/c) #168/2=84
                diff=decimal-diff #99-84
                print(''.join(list(reversed(str(diff))))[pos])
                break
        else:
                decimal = int(str(lim_init)*(c+1))
                lim+=int(str(lim_init)+'0'*c)*(c+1)

