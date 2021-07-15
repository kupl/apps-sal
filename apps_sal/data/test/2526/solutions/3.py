x,y,a,b,c=map(int,input().split())
p=sorted(list(map(int,input().split())))[::-1][:x]
q=sorted(list(map(int,input().split())))[::-1][:y]
r=sorted(list(map(int,input().split())))[::-1]
r=r[:min(len(r),x+y)]
l=sum([p,q,r],[])
print(sum(sorted(l)[::-1][:x+y]))
