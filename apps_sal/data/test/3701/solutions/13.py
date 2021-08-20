def count_components(line):
    in_zero_component = False
    num_components = 0
    for c in line:
        if c == '0':
            if not in_zero_component:
                num_components += 1
            in_zero_component = True
        else:
            in_zero_component = False
    return num_components


(_, reverse_cost, invert_cost) = [int(x) for x in input().split()]
line = input()
num_components = count_components(line)
cost = (num_components - 1) * min(reverse_cost, invert_cost) + invert_cost if num_components > 0 else 0
print(cost)
