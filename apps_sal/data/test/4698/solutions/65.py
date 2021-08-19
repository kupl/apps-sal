N = int(input())
T = list(map(int, input().split()))
M = int(input())
drink = []
for i in range(M):
    (P, X) = map(int, input().split())
    drink.append([P, X])
for j in range(len(drink)):
    (P, X) = drink[j]
    time = X + sum(T) - T[P - 1]
    print(time)
