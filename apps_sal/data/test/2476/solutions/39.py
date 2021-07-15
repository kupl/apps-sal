
N = int(input())

A = list(map(int,input().split()))

dic = {}

for a in A:

    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

B = []
for i in dic:
    B.append(dic[i])

B.sort()

B_sub = B.copy()

for i in range(len(B)-1):
    B_sub[i+1] += B_sub[i] 

aind = N + 1
nind = len(B) - 1

#print (B,B_sub)

for i in range(N):

    i += 1

    while True:

        while nind > 0 and B[nind] > aind - 1:

          nind -= 1

        if i > len(B):
            print((0))
            break

        elif ((len(B) - 1) - nind ) * (aind-1) + B_sub[nind] >= (aind - 1) * i:
            print((aind - 1))
            break

        aind -= 1


