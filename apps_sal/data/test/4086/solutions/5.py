# ANSHUL GAUTAM
# IIIT-D


T = int(input())
l = list(map(int, input().split()))
L = []
r = l[::-1]
for i in r:
    if(i not in L):
        L.append(i)
R = L[::-1]
print(len(R))
print(*R)
