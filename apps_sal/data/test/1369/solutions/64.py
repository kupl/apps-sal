import math

epsilon = 5 * 10 ** (-7)

N = int(input())
xys = [tuple(map(int, input().split())) for _ in range(N)]
xs, ys = zip(*xys)

lsd = 0  #longest squared distance
for i in range(0, N):
    for j in range(i+1, N):
        sd = (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2 
        if lsd < sd:
            lsd = sd
            farthest_2_points = (i, j)

#try a circle that has a line connecting farthest 2 points as a diameter.
p, q = farthest_2_points
center_x = (xs[p] + xs[q]) / 2
center_y = (ys[p] + ys[q]) / 2
all_in_circle = True
for i in range(N):
    if (xs[i] - center_x)**2 + (ys[i] - center_y)**2 > lsd / 4 + epsilon:
        all_in_circle = False

if all_in_circle:
    #We want the radius, not the diameter.
    print(lsd ** 0.5 / 2)
    return

#If failed, then try any circles that has 3 or more points on the edge.
smallest_radius = 10 ** 9
for p in range(0, N):
    for q in range(p+1, N):
        for r in range(q+1, N):
            #vec1 = (xs[p] - xs[r], ys[p] - ys[r])
            #vec2 = (xs[q] - xs[r], ys[q] - ys[r])
            pq = ((xs[q] - xs[p])**2 + (ys[q] - ys[p])**2)**0.5
            v1x = xs[p] - xs[r]
            v1y = ys[p] - ys[r]
            v2x = xs[q] - xs[r]
            v2y = ys[q] - ys[r]
            vec1_len = (v1x**2 + v1y**2)**0.5
            vec2_len = (v2x**2 + v2y**2)**0.5
            vecs_dot = v1x*v2x + v1y*v2y
            theta = math.acos(min(1.0, max(-1.0, vecs_dot / (vec1_len * vec2_len))))
            if theta == 0:
                continue
            radius = pq / (2 * math.sin(theta))

            #calculate where the center is
            det = v1x * v2y - v1y * v2x
            if det == 0:
                continue
            center_x = xs[r] + (   v2y  * vec1_len**2 + (-v1y) * vec2_len**2) / (2 * (det))
            center_y = ys[r] + ( (-v2x) * vec1_len**2 +   v1x  * vec2_len**2) / (2 * (det))
            all_in_circle = True
            for s in range(N):
                if ((xs[s] - center_x)**2 + (ys[s] - center_y)**2)**0.5 > radius + epsilon:
                    all_in_circle = False
            if all_in_circle:
                smallest_radius = min(smallest_radius, radius)
print(smallest_radius)
