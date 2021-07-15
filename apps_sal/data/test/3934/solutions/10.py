n = int(input())

nodes = [0]*n

for i in range (0,n-1):
    for x in map(int,input().split()):
        nodes[x-1] += 1

if 2 in nodes:
    print("NO")

else:
    print("YES")

