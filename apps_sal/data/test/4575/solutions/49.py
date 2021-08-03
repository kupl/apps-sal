N = int(input())
D, X = map(int, input().split())
d = {}
for i in range(1, N + 1):
    d[i] = int(input())

pieces = 0
for day in range(1, D + 1):
    for person in range(1, N + 1):
        if (day - 1) % d[person] == 0:
            pieces += 1

pieces += X
print(pieces)
