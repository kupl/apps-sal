counts = [int(x) for x in input().split()]
n = int(input())
sizes = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
size_to_i = {size: i for i, size in enumerate(sizes)}
two_sizes = {(x, y): [] for x, y in zip(list(range(6)), list(range(1, 7)))}

decision = [''] * n

for i in range(n):
    demand = [size_to_i[size] for size in input().split(',')]
    if len(demand) == 1:
        d = demand[0]
        counts[d] -= 1
        decision[i] = sizes[d]
    else:
        two_sizes[(demand[0], demand[1])].append(i)

for smaller, larger in zip(list(range(5)), list(range(1, 6))):
    for part in two_sizes[(smaller, larger)]:
        to_give = smaller if counts[smaller] > 0 else larger
        counts[to_give] -= 1
        decision[part] = sizes[to_give]


def possible():
    for c in counts:
        if c < 0:
            return False
    return True


if possible():
    print('YES')
    for d in decision:
        print(d)
else:
    print('NO')
