(a, b) = list(map(int, input().split()))
x = b - a
tower = 0
for i in range(1, x + 1):
    tower += i
print(tower - b)
