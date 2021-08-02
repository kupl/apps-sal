from functools import reduce

n, q = [int(x) for x in input().split()]

substitutions = {}

for _ in range(q):
    from_str, to_str = input().split()

    if to_str in substitutions:
        substitutions[to_str].append(from_str)
    else:
        substitutions[to_str] = [from_str]


def generate_str(start_str):
    if len(start_str) == n:
        return 1

    if start_str[0] not in substitutions:
        return 0

    result = 0
    for variant in substitutions[start_str[0]]:
        result += generate_str(variant + start_str[1:])

    return result


print(generate_str('a'))
