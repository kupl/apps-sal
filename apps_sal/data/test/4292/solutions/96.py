n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
sm = 0
for i in range(k):
    sm += l[i]
print(sm)
