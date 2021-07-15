N,K = (int(T) for T in input().split())
Per = [int(T) for T in input().split()]
Wat = 0
for X in range(0,N-1):
    if Per[X]+K<=Per[X+1]:
        Wat += K
    else:
        Wat += Per[X+1]-Per[X]
print(Wat+K)
