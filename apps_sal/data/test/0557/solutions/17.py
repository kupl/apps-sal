n, m = [int(v) for v in input().split()]
teleports = []
for _ in range(n):
    a, b = [int(v) for v in input().split()]
    teleports.append((a, b))

reachable = [False] * (m + 1)
reachable[0] = True

for a, b in teleports:
    if reachable[a]:
        for i in range(a + 1, b + 1):
            reachable[i] = True

print(["NO", "YES"][reachable[m]])

