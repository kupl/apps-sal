n = int(input())
d, x = map(int, input().split())
a = [int(input())for _ in [0] * n]
sm = 0
for i in range(n):
    j = 1
    while j <= d:
        sm += 1
        j = j + a[i]
print(sm + x)
