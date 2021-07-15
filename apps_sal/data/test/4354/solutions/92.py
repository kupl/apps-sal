n, m = list(map(int,input().split()))
s_x_plus_y = []
s_x_minus_y = []
p_x_plus_y = []
p_x_minus_y = []

for student in range(n):
    x, y = list(map(int,input().split()))
    s_x_plus_y.append(x + y)
    s_x_minus_y.append(x - y)

for i in range(m):
    x, y = list(map(int,input().split()))
    p_x_plus_y.append(x + y)
    p_x_minus_y.append(x - y)


for i in range(n):
    p_dist = []
    for j in range(m):
        p1 = abs(s_x_plus_y[i] - p_x_plus_y[j])
        p2 = abs(s_x_minus_y[i] - p_x_minus_y[j])
        d = max(p1, p2)
        p_dist.append(d)
    print((p_dist.index(min(p_dist))+1))

