n = int(input())
a1 = input()
a2 = input()
sm = 0
for i in range(n):
    q = int(a1[i])
    w = int(a2[i])
    sm += min(abs(q - w), min(q, w) + 10 - max(q, w))
print(sm)
