(n, m) = map(int, input().split())
ques = list(map(int, input().split()))
acutions = set(map(int, input().split()))
acu = []
points = 0
for i in range(n):
    if i + 1 in acutions:
        acu.append(ques[i])
    else:
        points += ques[i]
acu.sort(reverse=True)
for a in acu:
    if points > a:
        points += points
    else:
        points += a
print(points)
