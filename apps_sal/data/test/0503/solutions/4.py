def get_sequence(a_indices, b_indices, c_indices):
    a_i, b_i, c_i = 0, 0, 0
    i = 0
    total = len(a_indices) + len(b_indices) + len(c_indices)
    a_indices = a_indices[:]
    b_indices = b_indices[:]
    c_indices = c_indices[:]

    a_indices.append(1000005001)
    b_indices.append(1000005001)
    c_indices.append(1000005001)
    sequence = []
    while i < total:
        minimum = calculate_minimum(a_indices[a_i], b_indices[b_i], c_indices[c_i])
        if minimum == 'a':
            a_i += 1
        elif minimum == 'b':
            b_i += 1
        elif minimum == 'c':
            c_i += 1
        sequence.append(minimum)
        i += 1

    return sequence


def calculate(a_indices, b_indices, c_indices):
    sequence = get_sequence(a_indices, b_indices, c_indices)

    a_stack, b_stack, c_stack = 0, 0, 0

    for ch in sequence:
        if ch == 'a':
            a_stack += 1
        elif ch == 'b':
            b_stack += a_stack
        elif ch == 'c':
            c_stack += b_stack

    return c_stack


def calculate_minimum(a_index, b_index, c_index):
    if a_index < b_index:
        if a_index < c_index:
            return 'a'
        else:
            return 'c'
    else:
        if b_index < c_index:
            return 'b'
        else:
            return 'c'


def main():
    n, k = [int(t) for t in input().split()]
    a_list = [int(t) for t in input().split()]
    hash_map = {}
    for index, a in enumerate(a_list):
        if a in hash_map:
            hash_map[a].append(index)
        else:
            hash_map[a] = [index]

    total_gp = 0
    if k != 1:
        for a1 in list(hash_map.keys()):
            a2 = a1 * k
            a3 = a2 * k
            if a2 in hash_map and a3 in hash_map:
                total_gp += calculate(hash_map[a1], hash_map[a2], hash_map[a3])
    else:
        for a in list(hash_map.keys()):
            count = len(hash_map[a])
            if count >= 3:
                nc3 = count * (count - 1) / 2 * (count - 2) / 3
                total_gp += int(nc3)

    print(total_gp)


def __starting_point():
    main()

__starting_point()
