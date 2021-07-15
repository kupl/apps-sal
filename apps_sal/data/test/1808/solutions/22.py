N,K,X = map(int,input().split())
lst = sorted([int(i) for i in input().split()])

for i in range(1,K+1):
    lst[-i] = X
print(sum(lst))
