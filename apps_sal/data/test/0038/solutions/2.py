def calc_distances(points):
    distances = [0] * n
    for i in range(n):
        dist = points[i] - points[i - 1]
        if dist < 0:
            dist += length
        distances[i] = dist
    return distances


def rotate(lst, i):
    return lst[i:] + lst[:i]


n, length = list(map(int, input().split()))
a, b = [calc_distances(list(map(int, input().split()))) for i in range(2)]
for i in range(n):
    if b[i] == a[0] and rotate(b, i) == a:
        print("YES")
        break
else:
    print("NO")
