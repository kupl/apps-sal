n, k = list(map(int, input().split()))
V = list(map(int, input().split()))


def get_jewelries(box, left_pop, right_pop):
    if left_pop + right_pop >= len(box):
        return box[:]

    left = box[:left_pop]
    right = box[-right_pop:] if right_pop else []

    return left + right


candidates = []
pop_max = min(k, n)
for pop_count in range(pop_max + 1):
    residue = k - pop_count

    for left_pop in range(pop_count + 1):
        right_pop = pop_count - left_pop
        jewelries = get_jewelries(V, left_pop, right_pop)
        jewelries.sort(reverse=True)

        for _ in range(residue):
            if not jewelries:
                break
            if jewelries[-1] < 0:
                jewelries.pop()

        value = sum(jewelries)
        candidates.append(value)

print((max(candidates)))
