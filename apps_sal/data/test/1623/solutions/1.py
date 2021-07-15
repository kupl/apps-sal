n,l,r=list(map( int ,input().split() ))
s= (pow(2 , r) -1  ) + ( (n-r)*pow(2,r-1) )
m =( pow(2,l) -1 ) +( (n-l) )
print(m,s)

