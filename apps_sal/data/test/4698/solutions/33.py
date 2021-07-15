N = input()
T = [int(x) for x in input().split()]
M = int(input())
Drink = [tuple(map(int,input().split())) for _ in range(M)]
sumT = sum(T)
for p,x in Drink:
    print(sumT-T[p-1]+x)
