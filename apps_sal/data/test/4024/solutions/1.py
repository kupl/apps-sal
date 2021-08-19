import queue
(n, k) = [int(el) for el in input().split()]
s = input()


def sol_e(line, set_size):
    unique_set = {line}
    cost = 0
    lines_queue = queue.Queue()
    lines_queue.put(line)
    cur_set_size = 1
    while cur_set_size < set_size:
        cur_line = lines_queue.get()
        for index in range(len(cur_line)):
            new_line = cur_line[:index] + cur_line[index + 1:]
            if new_line not in unique_set:
                unique_set.add(new_line)
                cost += len(line) - len(new_line)
                cur_set_size += 1
                lines_queue.put(new_line)
                if cur_set_size == set_size:
                    return cost
        if lines_queue.empty():
            return -1
    return cost


print(sol_e(s, k))
