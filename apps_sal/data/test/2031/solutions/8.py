n = int(input())
a = [int(x) for x in input().split()]
a_sorted = sorted(a, reverse=True)

m = int(input())
for i in range(m):
    k, pos = [int(x) for x in input().split()]

    vals = a_sorted[0:k]

    result = []
    for val in a:
        if val in vals:
            result.append(val)
            vals.remove(val)

        if len(vals) == 0:
            break

    print(result[pos - 1])



