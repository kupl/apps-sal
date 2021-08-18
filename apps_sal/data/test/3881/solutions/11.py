
import collections
import itertools


Operation = collections.namedtuple("Operation", "from_str to_str")


def is_feasible_operation(base_str, operation):
    return base_str.startswith(operation.from_str)


def conduct_operation(base_str, operation):
    return base_str.replace(operation.from_str, operation.to_str, 1)


def breadth_first_search(init_str, operations):
    q = collections.deque()
    q.append(init_str)
    visited = collections.defaultdict(bool)
    visited[init_str] = True
    while q:
        base_str = q.popleft()
        if base_str == "a":
            return True
        for operation in operations:
            if not is_feasible_operation(base_str, operation):
                continue
            new_str = conduct_operation(base_str, operation)
            if not visited[new_str]:
                visited[new_str] = True
                q.append(new_str)
    return False


def count_valid_strings(len_str, operations):
    counter = 0
    for chars in itertools.product("abcdef", repeat=len_str):
        init_str = "".join(chars)
        if breadth_first_search(init_str, operations):
            counter += 1
    return counter


def main():
    n, q = list(map(int, input().split()))
    operations = [Operation(*input().split()) for _ in range(q)]
    print(count_valid_strings(n, operations))


def __starting_point():
    main()


__starting_point()
