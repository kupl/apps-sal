n,m=[int(i) for i in input().split()]
x=1-1/(2**m)
t=1900*m+100*(n-m)
print(int(t/((2**m)*((1-x)**2))))
