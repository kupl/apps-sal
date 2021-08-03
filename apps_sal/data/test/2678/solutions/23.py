from sys import stdin
n = int(stdin.readline())
sets = []
for i in range(n):
    sets.append(tuple(map(int, stdin.readline().split())))
sets.sort()
ans = 1
last_end = sets[0][1]
for i in range(1, len(sets)):
    if last_end < sets[i][0]:
        ans += 1
        last_end = sets[i][1]
    else:
        last_end = min(last_end, sets[i][1])
print(ans)
