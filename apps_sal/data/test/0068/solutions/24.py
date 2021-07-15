import functools

n = int(input())
dct = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
moves_list = list([dct[x] for x in [*input()]])
dest_x, dest_y = list(map(int, input().split()))


def add_vectors(a, b):
    return a[0] + b[0], a[1] + b[1]


def subtract_vectors(a, b):
    return a[0] - b[0], a[1] - b[1]


total = functools.reduce(add_vectors, moves_list)


def czy(dl) -> bool:
    sumo = total
    for v in moves_list[:dl]:
        sumo = subtract_vectors(sumo, v)
    for i in range(1, n - dl + 2):
        (dx, dy) = list(map(abs, subtract_vectors((dest_x, dest_y), sumo)))
        if dx + dy <= dl and (dx + dy) % 2 == dl % 2:
            return True
        if i + dl - 1 >= n:
            break
        sumo = subtract_vectors(sumo, moves_list[i + dl - 1])
        sumo = add_vectors(sumo, moves_list[i - 1])
    return False


pocz = 0
kon = n
while pocz < kon:
    sr = (pocz + kon) // 2
    if czy(sr):
        kon = sr
    else:
        pocz = sr + 1

if czy(pocz):
    print(pocz)
else:
    print(-1)

