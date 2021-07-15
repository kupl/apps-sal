k=int(input())
print((k//2)**2 if k&1!=1 else (k+1)//2 * ((k+1)//2-1))
