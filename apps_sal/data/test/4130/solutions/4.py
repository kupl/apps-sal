n = int(input())
r = [int(x) for x in input().split()]
r.sort()
t = 0
boxers = 0
for i in range(n):
    if r[i] > t + 1:
        boxers += 1
        t = r[i] - 1
    elif r[i] == t + 1:
        boxers += 1
        t = r[i]
    elif r[i] == t:
        boxers += 1
        t = r[i] + 1
print(boxers)
