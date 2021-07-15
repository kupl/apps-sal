from collections import defaultdict
N=int(input())
A = {}
B = {}
for a in "ATGC":
    for b in "ATGC":
        for c in "ATGC":
            if a+b+c not in ["AGC", "ACG", "GAC"]:
                B[a+b+c] = 1
X=set()
for a in "ATGC":
    for b in "ATGC":
        for c in "ATGC":      
            for d in "ATGC":
                s=a+b+c+d
                t=b+a+c+d
                u=a+c+b+d
                v=a+b+d+c
                if any(["AGC" in x for x in [s,t,u,v]]):
                    X.add(s)

for _ in range(N-3):
    A = B
    B = defaultdict(int)
    for k in A:
        for l in "ATGC":
            if k+l not in X:
                B[k[1:]+l] += A[k]
    
print(sum(B.values())%(10**9+7))
