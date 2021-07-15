n = int(input())

days = [list(map(int, input().split())) for i in range(n)]
days.sort()

L = [0]
for i in range(n):
    if days[i][1] >= L[i]:
        L.append(days[i][1])
    else:
        L.append(days[i][0])

print(L[-1])

