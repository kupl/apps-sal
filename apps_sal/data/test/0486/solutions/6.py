def f(x):
    if x[0]=='1':
        return 9**(len(x)-1)
    elif len(x)==1:
        return int(x)
    else:
        return max((int(x[0])-1)*9**(len(x)-1),int(x[0])*f(x[1:]))
n=input('')
print(f(n))

