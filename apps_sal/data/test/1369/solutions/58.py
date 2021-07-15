from itertools import combinations

epsilon = 5 * 10 ** (-7)

N = int(input())
#Get points as complex numbers like x + yi.
points = [complex(*list(map(int, input().split()))) for _ in range(N)]


#try a circle that has a line connecting farthest 2 points as a diameter.
longest_radius = 0
for p, q in combinations(points, 2):
    radius = abs(p - q) / 2
    if longest_radius < radius:
        longest_radius = radius
        center = (p + q) / 2

out_of_circle = False
for s in points:
    if abs(s - center) > longest_radius + epsilon:
        out_of_circle = True
        break

if not out_of_circle:
    print(longest_radius)
    return


#If failed, then try any circles that has 3 or more points on the edge.
smallest_radius = 10 ** 9
for p, q, r in combinations(points, 3):
    denominator = (p-q)*r.conjugate() + (q-r)*p.conjugate() + (r-p)*q.conjugate()
    if denominator == 0 + 0j:
        continue
    numerator = (p-q)*(abs(r)**2) + (q-r)*(abs(p)**2) + (r-p)*(abs(q)**2)
    center = numerator/denominator
    radius = abs(p - center)

    for s in points:
        if abs(s - center) > radius + epsilon:
            break
    else:
        smallest_radius = min(smallest_radius, radius)

print(smallest_radius)

