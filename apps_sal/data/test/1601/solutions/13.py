n = int(input())
sentinel = [(10**9, 10**9, 10**9)]
points = sorted(tuple(map(int, input().split())) + (i,) for i in range(1, n + 1)) + sentinel
ans = []
rem = []

i = 0
while i < n:
    if points[i][:2] == points[i + 1][:2]:
        ans.append(f'{points[i][-1]} {points[i+1][-1]}')
        i += 2
    else:
        rem.append(i)
        i += 1

rem += [n]
rem2 = []

n = len(rem)
i = 0
while i < n - 1:
    if points[rem[i]][0] == points[rem[i + 1]][0]:
        ans.append(f'{points[rem[i]][-1]} {points[rem[i+1]][-1]}')
        i += 2
    else:
        rem2.append(points[rem[i]][-1])
        i += 1

print(*ans, sep='\n')
for i in range(0, len(rem2), 2):
    print(rem2[i], rem2[i + 1])
