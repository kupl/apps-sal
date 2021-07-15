m,b=list(map(int,input().split()))
bn=0
for i in range(b):
  bn=max(bn,(m*(b-i)*(m*(b-i)+1)//2)*(i+1)+i*(i+1)//2*(m*(b-i)+1))
print(bn)

