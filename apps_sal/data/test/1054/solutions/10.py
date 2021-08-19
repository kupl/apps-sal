n = int(input())
mx = 10000000000
my = 10000000000
vx = -10000000000
vy = -10000000000
for i in range(n):
    (a, b) = map(int, input().split())
    mx = min(mx, a)
    vx = max(vx, a)
    my = min(my, b)
    vy = max(vy, b)
print(max(vx - mx, vy - my) * max(vx - mx, vy - my))
