foo = list(input().split())
K = int(foo[1])
P = sorted(map(int,list(input().split())))
i=0
total = int(0)
while i < K:
    total = total + int(P[i])
    i+=1
print(total)
