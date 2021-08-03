n = int(input())
a = []
team = [None] * (n + n)
for i in range(1, n + n):
    for j, v in enumerate(map(int, input().split())):
        a.append((v, i, j))
a.sort(reverse=True)

for _, i, j in a:
    if team[i] is None and team[j] is None:
        team[i] = j + 1
        team[j] = i + 1

print(' '.join(str(i) for i in team))
