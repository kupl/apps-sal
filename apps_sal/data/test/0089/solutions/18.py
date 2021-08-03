n = int(input())
sm = 0
for i in range(n, -1, -2):
    sm += i
    if n <= 2:
        break
print(sm)
