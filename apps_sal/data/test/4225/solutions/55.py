cards=input()
new=cards.split()
a=int(new[0])
b=int(new[1])
c=int(new[2])
k=int(new[3])
if a>k:
    print(k)
else:
    if a+b>k:
        print(a)
    else:
        sum=a+(k-(a+b))*(-1)
        print(sum)

