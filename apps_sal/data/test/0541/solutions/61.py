import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bridges = []
for _ in range(M):
    a, b = map(int, input().split())
    bridges.append([a, b])

bridges.sort(key=lambda x: x[1])

p = 0
t = 0

while len(bridges) > 0:
    t = bridges[0][1]
    p += 1
    bridges = [i for i in bridges if i[0] >= t]

print(p)
