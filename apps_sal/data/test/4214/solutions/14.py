import itertools

n = int(input())

town = []

for i in range(n):
    x,y = map(int, input().split())
    town.append((x,y))

cnt = 0
length = 0

for t in itertools.permutations(town):
    for i in range(n-1):
        x = (t[i][0]-t[i+1][0])**2
        y = (t[i][1]-t[i+1][1])**2
        length += (x+y)**0.5
    cnt += 1

print(length/cnt)
