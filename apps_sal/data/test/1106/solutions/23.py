import fileinput


def parent_id(elem_id):
    return int(elem_id / 2)


def children_ids(elem_id):
    return elem_id * 2, elem_id * 2 + 1


def solve(lights):
    def solve_subtree(root_id):
        a, b = children_ids(root_id)
        if a >= len(lights):
            # print(root_id, "is leaf and has", lights[root_id], "lights")
            return (0, lights[root_id])
        else:
            needed_a, val_a = solve_subtree(a)
            needed_b, val_b = solve_subtree(b)
            max_val = max(val_b, val_a)
            # print(root_id, "has", val_a, "and", val_b, "in subtrees, totally needs",
            #     (needed_a + needed_b + (2 * max_val - (val_a + val_b))), "lights")
            return (needed_a + needed_b + (2 * max_val - (val_a + val_b)),
                    max_val + lights[root_id])
    needed, val = solve_subtree(1)
    return needed


def __starting_point():
    data = list(iter(fileinput.input()))
    lights = [0, 0] + list(map(int, data[1].split()))
    print(solve(lights))


__starting_point()
