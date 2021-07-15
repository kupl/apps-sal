n,m,k=[int(i) for i in input().split()]
ryad=k//(2*m)+1
if k%(2*m)==0:
    ryad-=1
parta=(k-2*m*(ryad-1))//2+k%2
if k%2==0:
    mesto='R'
else:
    mesto='L'
print(ryad,parta,mesto)
