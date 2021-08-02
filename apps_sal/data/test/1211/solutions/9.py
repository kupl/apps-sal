def read_nums():
    return [int(x) for x in input().split()]


def get_res(num_hamsters, box_sizes):
    min_index, res_box_size, min_left = 0, box_sizes[0], num_hamsters % box_sizes[0]
    for index, box_size in enumerate(box_sizes):
        cur_left = num_hamsters % box_size
        if cur_left < min_left:
            min_left = cur_left
            min_index = index
            res_box_size = box_size
    return min_index, num_hamsters // res_box_size


def main():
    num_hamsters, num_box_types = read_nums()
    box_sizes = read_nums()
    box_index, num_boxes = get_res(num_hamsters, box_sizes)
    print(box_index + 1, num_boxes)


def __starting_point():
    main()


__starting_point()
