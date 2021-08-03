n, m = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([int(x) for x in input().split()])

print(max(min(Xi) for Xi in X))
