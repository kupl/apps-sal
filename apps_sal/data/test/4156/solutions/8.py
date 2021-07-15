stops,m = list(map(int,input().split()))
people = [int(i) for i in input().split()]

cM = 0
cm = 0
c = 0
for i in range(stops):
    c += people[i]
    if c > cM:
        cM = c
    if c <cm:
        cm = c

print(m-cM+cm+1 if m-cM+cm+1>=1 else 0)

