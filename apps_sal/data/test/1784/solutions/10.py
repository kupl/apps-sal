n, k = map(int, input().split())
data = list(map(int, input().split()))

need = 0
res = [list() for _ in range(n)]


def custom_min(data):
    min = None
    for x in data:
        if min is None or x < min:
            min = x

    return 1 if min == 0 else min


def not_all_zeros(data):
    for x in data:
        if x != 0:
            return True
    return False


color = 1
min_v = custom_min(data)

while not_all_zeros(data) != 0:
    min_v = custom_min(data)

    if color > k:
        print("NO")
        break

    for i in range(len(data)):
        if data[i] != 0:
            val = min_v + 1 if (data[i] > min_v and color == 1) else min_v
            data[i] -= val
            res[i].append((color, val))

    color += 1
else:
    print('YES')
    for l in res:
        s = []

        for x in l:
            s += [str(x[0])] * x[1]

        print(' '.join(s))
