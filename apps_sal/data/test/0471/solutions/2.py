def calc_dist(coords, a):
    if len(coords) == 0:
        return 0
    
    if a > coords[-1]:
        return a - coords[0]
    if a < coords[0]:
        return coords[-1] - a
    
    return coords[-1] - coords[0] + min(a - coords[0], coords[-1] - a)


n, a = list(map(int, input().split()))

coords = list(map(int, input().split()))

coords.sort()

#~ print(coords[:-1], coords[1:])

print(min(calc_dist(coords[:-1], a), calc_dist(coords[1:], a)))

