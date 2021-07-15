n=int(input())
p=[int(x) for x in input().split()]
for i in range (0,n):
    p[i]=str(bin(p[i])).count('1')
s=set(p)
t=0
for j in s:
    t+=p.count(j)*(p.count(j)-1)/2
print(int(t))










