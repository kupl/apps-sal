(n, h) = list(map(int, input().split()))
l = list(map(int, input().split()))
sm = 0
for x in l:
    sm += 1
    if x > h:
        sm += 1
print(sm)
