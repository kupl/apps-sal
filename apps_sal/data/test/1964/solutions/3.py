kasses = int(input())
sizes = list(map(int, input().split()))
ocheredi = []

for i in range(kasses):
    ocheredi.append(list(map(int, input().split())))

m = -1

for i in ocheredi:
    cm = 15 * len(i)
    for j in i:
        cm += 5 * j
    if cm < m or m == -1:
        m = cm

print(m)
