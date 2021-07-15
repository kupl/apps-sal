# AtCoder Beginner Contest 131
# B - Bite Eating

N,L=map(int,input().split())
minabs=10**9
apples=[]
for i in range (N):
    t=L+i
    apples.append(t)
    if abs(t)<abs(minabs):
        minabs=t

full=sum(apples)

print(full-minabs)
