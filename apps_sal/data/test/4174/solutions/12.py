# AtCoder Beginner Contest 130
# B - Bounding
import bisect

N,X=map(int,input().split())
L=list(map(int,input().split()))

accumu_L=[0]

for i in range (N):
    accumu_L.append(accumu_L[-1]+L[i])

# print(accumu_L)

print(bisect.bisect_right(accumu_L,X))
