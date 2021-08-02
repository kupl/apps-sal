colors = ["SHIT"] + list(map(int, input().split()))

faces = [(1, 2, 3, 4), (5, 6, 7, 8),
         (9, 10, 11, 12), (13, 14, 15, 16),
         (17, 18, 19, 20), (21, 22, 23, 24)]


def is_good(colors):
    return all([all([colors[i] == colors[face[0]] for i in face]) for face in faces])


rotations = {(1, 2, 3, 4): ([13, 5, 17, 21], [14, 6, 18, 22]),
             (5, 6, 7, 8): ([14, 9, 19, 4], [16, 10, 17, 3]),
             (9, 10, 11, 12): ([7, 15, 23, 19], [8, 16, 24, 20]),
             (13, 14, 15, 16): ([5, 1, 24, 9], [7, 3, 22, 11]),
             (17, 18, 19, 20): ([6, 10, 23, 2], [8, 12, 21, 4]),
             (21, 22, 23, 24): ([1, 18, 12, 15], [2, 20, 11, 13]), }


def rotate(colors, face):
    result1 = colors.copy()
    rule1, rule2 = rotations[face]
    for i in range(4):
        result1[rule1[i]] = colors[rule1[(i + 1) % 4]]
        result1[rule2[i]] = colors[rule2[(i + 1) % 4]]

    result2 = colors.copy()
    for i in range(4):
        result2[rule1[(i + 1) % 4]] = colors[rule1[i]]
        result2[rule2[(i + 1) % 4]] = colors[rule2[i]]
    return (result1, result2)


for face in faces:
    rotated = rotate(colors, face)
    if is_good(rotated[0]) or is_good(rotated[1]):
        print("YES")
        break
else:
    print("NO")
