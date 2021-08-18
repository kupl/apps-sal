
total_weight, children, at_least_one = [int(x) for x in input().split()]


at_least_weights = [0] * (total_weight + 1)
not_least_weights = [0] * (total_weight + 1)
if total_weight < at_least_one:
    print(0)
elif total_weight == at_least_one:
    print(1)
else:
    not_least_weights[0] = 1
    for x in range(1, total_weight + 1):
        for y in range(1, at_least_one):
            if x - y >= 0:
                not_least_weights[x] += not_least_weights[x - y]
                at_least_weights[x] += at_least_weights[x - y]
        for z in range(at_least_one, children + 1):
            if x - z >= 0:
                at_least_weights[x] += at_least_weights[x - z]
                at_least_weights[x] += not_least_weights[x - z]
    print(at_least_weights[total_weight] % 1000000007)
