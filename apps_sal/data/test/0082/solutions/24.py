3.5
n,k=[int(x) for x in input().split()]
mas=[int(x) for x in input().split()]

p=0
s=sum(mas)
while True:
    if s/n>=k-0.5:
        print(p)
        quit()
    else:
        s+=k
        n+=1
        p+=1
