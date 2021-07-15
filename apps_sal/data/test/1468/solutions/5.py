def g(c,d):
    s=0
    while s<len(a[d]) and a[c][s]==a[d][s]:s+=1
    a[c]=a[c][:s]

def f(a):
    for i in range(len(a)-1,0,-1):
        if a[i-1]>a[i]:g(i-1,i)
    print('\n'.join(a))

n=int(input())
a=[input()for i in range(n)]
f(a)



