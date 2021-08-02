N, M = list(map(int, input().split()))
start = set()
goal = set()

for i in range(M):
    a, b = list(map(int, input().split()))
    if(a == 1):
        start.add(b)
    elif(b == N):
        goal.add(a)
print(("IMPOSSIBLE" if(len(start & goal) == 0) else "POSSIBLE"))
