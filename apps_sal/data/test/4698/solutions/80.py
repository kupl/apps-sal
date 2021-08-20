N = int(input())
times = list(map(int, input().split()))
M = int(input())
drinks = []
for _ in range(M):
    drinks.append(list(map(int, input().split())))
for drink in drinks:
    total = 0
    for j in range(N):
        if drink[0] == j + 1:
            total += drink[1]
        else:
            total += times[j]
    print(total)
