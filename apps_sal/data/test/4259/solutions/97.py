k=int(input());a,b=map(int,input().split())
print('NOGK'[any([i%k==0 for i in range(a,b+1)])::2])
