(n, m, k) = [int(s) for s in input().split(' ')]
hole_locations = [int(s) for s in input().split(' ')]
hole_array = [0] * n
for hole in hole_locations:
    hole_array[hole - 1] += 1
bone = 1
if hole_array[0] == 1:
    print(bone)
else:
    for i in range(1, k + 1):
        (u, v) = [int(s) for s in input().split(' ')]
        if u == bone:
            bone = v
            if hole_array[v - 1] == 1:
                break
        elif v == bone:
            bone = u
            if hole_array[u - 1] == 1:
                break
    print(bone)
