stones = int(input())
costs = list(map(int, input().split(' ')))
reg = costs[:]
costs.sort()
a = [0] + [0] * stones
b = [0] + [0] * stones
for i in range(1, stones + 1):
    a[i] = a[i-1] + costs[i-1]
    b[i] = b[i-1] + reg[i-1]
    
for i in range(int(input())):
    x, y, z = list(map(int, input().split(' ')))
    if x == 2:
        print(a[z] - a[y-1])
    else:
        print(b[z] - b[y-1])

