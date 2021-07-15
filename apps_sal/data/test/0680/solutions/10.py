coords1 = tuple(map(int, input().split()))
coords2 = tuple(map(int, input().split()))
coords3 = tuple(map(int, input().split()))
coords = [coords1, coords2, coords3]
coords.sort(key=(lambda x: x[0]))


def min_path(coords_lm, coords_rm, coords_center):
    first_path = []
    second_path = []
    first_path.append(tuple(coords_lm))
    while first_path[-1][0] != coords_center[0]:
        new_square = (first_path[-1][0] + 1, first_path[-1][1])
        first_path.append(new_square)

    orient = 1 if first_path[-1][1] < coords_center[1] else -1
    while first_path[-1][1] != coords_center[1]:
        new_square = (first_path[-1][0], first_path[-1][1] + 1*orient)
        first_path.append(new_square)

    second_path.append(tuple(coords_rm))
    while second_path[-1][0] != coords_center[0]:
        new_square = (second_path[-1][0] - 1, second_path[-1][1])
        second_path.append(new_square)

    orient = 1 if second_path[-1][1] < coords_center[1] else -1
    while second_path[-1][1] != coords_center[1]:
        new_square = (second_path[-1][0], second_path[-1][1] + 1*orient)
        second_path.append(new_square)

    return set(first_path).union(set(second_path))


path = min_path(coords[0], coords[2], coords[1])
path = list([" ".join((str(x[0]), str(x[1]))) for x in list(path)])
print(len(path))
print("\n".join(path))

