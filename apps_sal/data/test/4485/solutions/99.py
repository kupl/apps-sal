n, m = map(int, input().split())
start = [0] * 200001
goal = [0] * 200001

for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        if goal[b] == 1:
            print("POSSIBLE")
            return
        start[b] = 1
        a
    elif b == n:
        if start[a] == 1:
            print("POSSIBLE")
            return
        goal[a] = 1
print("IMPOSSIBLE")
