N = list(map(int,input().split()))
P = list(map(int,input().split()))
print(sum(sorted(P)[:N[1]]))
