a, b = map(int, input().split())
m = b - a
t = 0
for i in range(m):
    t += i
print(t - a)
