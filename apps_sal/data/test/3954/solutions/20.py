import os
if not("BEFUNGEE_HOME" in os.environ.keys()):
    f=open("input.txt","r")
    input=f.readline
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))

def f(l,r):
    original_sequence=a[l:r+1]
    outside_sequence=a[:l]+a[r+1:]
    original_sequence.sort()
    outside_sequence.sort(reverse=True)
    k_=min(k,len(original_sequence),len(outside_sequence))
    original_sequence[:k_]=[max(x,y) for x,y in zip(original_sequence[:k_],outside_sequence[:k_])]
    s=sum(original_sequence)
    return s

result=-2000000
for l in range(n):
    for r in range(l,n):
        result=max(f(l,r),result)

print(result)
