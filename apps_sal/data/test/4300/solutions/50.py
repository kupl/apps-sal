n = int(input())
d = list(map(int, input().split()))
sm = 0
for i in range(len(d) - 1):
    for j in range(i + 1, len(d)):
        sm += d[i] * d[j]
print(sm)
