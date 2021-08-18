def children_to_slices(n, k, l):
    kid_to_slice = [[]] * (k + 1)
    remaining = set([i for i in range(1, (n * k) + 1)])

    for item in l:
        kid_to_slice[item[0]] = kid_to_slice[item[0]] + [item[1]]
        remaining.remove(item[1])

    for i in range(1, k + 1):
        while len(kid_to_slice[i]) < n:
            kid_to_slice[i] = kid_to_slice[i] + [remaining.pop()]

    return kid_to_slice


first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])
l = []
assignments = [int(item) for item in input().split()]
for i in range(len(assignments)):
    l.append((i + 1, assignments[i]))

m = children_to_slices(n, k, l)
for i in range(1, k + 1):
    output = ""
    for item in m[i]:
        output += str(item) + " "
    print(output)
