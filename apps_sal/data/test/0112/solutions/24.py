n = int(input())
cubes = []
for i in range(n):
    cubes.append(list(map(int, input().split())))

taken = []
for i in range(10000):
    taken.append(0)

res = 0
for cube in cubes:
    for face in cube:
        taken[face] += 1

for cube1 in cubes:
    for cube2 in cubes:
        if cube1 != cube2:
            for face1 in cube1:
                for face2 in cube2:
                    tmp = str(face1) + str(face2)
                    taken[int(tmp)] += 1

for cube1 in cubes:
    for cube2 in cubes:
        for cube3 in cubes:
            if cube1 != cube2 and cube1 != cube3 and cube2 != cube3:
                for face1 in cube1:
                    for face2 in cube2:
                        for face3 in cube3:
                            tmp = str(face1) + str(face2) + str(face3)
                            taken[int(tmp)] += 1

iterate = 0
for i in taken:
    if i == 0 and iterate > 0:
        break

    res = iterate
    iterate += 1
print(res)
