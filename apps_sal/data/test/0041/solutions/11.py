n = int(input())
a = []
a = list(map(int, input().split()))

dist = pow(10, 9)
d = [dist] * len(a)

for i in range(len(a)):
    if(a[i] == 0):
        d[i] = 0
        dist = 0
    elif(dist < d[i]):
        dist += 1
        d[i] = dist

for i in range(len(a) - 1, -1, -1):
    # print(dist)
    if(a[i] == 0):
        d[i] = 0
        dist = 0
    elif(dist + 1 < d[i]):
        dist += 1
        d[i] = dist
for i in d:
    print(str(i) + ' ', end='')
