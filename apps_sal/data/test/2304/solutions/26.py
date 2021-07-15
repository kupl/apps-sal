n, m = list(map(int, input().split()))
vertices = {i: [] for i in range(n)}
for _ in range(m):
    l, r, d = list(map(int, input().split()))
    vertices[l - 1].append((r - 1, d))
    vertices[r - 1].append((l - 1, -d))


def answer():
    x = [None] * n

    for i in range(n):
        if x[i] is not None:
            continue
        x[i] = 0
        queue = [i]

        while queue:
            i0 = queue.pop()
            for i1, d in vertices[i0]:
                # print(i0, i1, x[i0], x[i1], d)
                if x[i1] is None:
                    x[i1] = x[i0] + d
                    queue.append(i1)
                elif x[i1] != x[i0] + d:
                    return False

    return True


if answer():
    print('Yes')
else:
    print('No')




