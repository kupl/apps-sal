
import collections
import itertools


GOAL = "a"
Operation = collections.namedtuple("Operation", "before after")


def is_possible_operation(original_str, operation):
    return original_str.startswith(operation.before)


def perform_operation(original_str, operation):
    return original_str.replace(operation.before, operation.after, 1)


def judge_dfs(initial_str, operations):
    stack = collections.deque()
    stack.append(initial_str)
    visited = collections.defaultdict(bool)
    visited[initial_str] = True
    while stack:
        original_str = stack.pop()
        if original_str == GOAL:
            return True
        for operation in operations:
            if is_possible_operation(original_str, operation):
                after_str = perform_operation(original_str, operation)
                if not visited[after_str]:
                    visited[after_str] = True
                    stack.append(after_str)
    else:
        return False


def count_valid_strings(len_init_str, operations):
    cands = itertools.product("abcdef", repeat=len_init_str)
    a = sum(1 for cs in cands if judge_dfs("".join(cs), operations))
    return a


def main():
    n, q = list(map(int, input().split()))
    operations = [Operation(*input().split()) for _ in range(q)]
    print(count_valid_strings(n, operations))


def __starting_point():
    main()


__starting_point()
