n = int(input())
u = []
v = []
for i in range(n):
    x, y = map(int, input().split())
    u.append(x + y)
    v.append(x - y)
    
u.sort()
v.sort()
print(max(u[-1] - u[0], v[-1] - v[0]))
