n,k=[int(i) for i in input().split()]
segment=list(range(1,n*k+1))
for i in range(n*k):
    segment[i]=str(segment[i])

num=[int(i) for i in input().split()]

for i in num:
    segment.remove(str(i))

t=0
for i in num:
    print(i,' '.join(segment[t:t+n-1]))
    t+=n-1

