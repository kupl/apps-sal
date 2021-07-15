L = [int(input()) for _ in range(4)]
print(L[2]*min(L[0],L[1])+L[3]*max(0,L[0]-L[1]))
