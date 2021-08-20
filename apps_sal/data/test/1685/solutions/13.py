from math import *
(n, q) = list(map(int, input().split()))
depth = int(log2(n + 1))


def get_layer(u):
    for layer in range(depth):
        if u % 2 ** (layer + 1) == 2 ** layer:
            return layer


def is_right_child(layer, u):
    return u % 2 ** (layer + 1) % 2 == 0


for x in range(q):
    u = int(input())
    layer = get_layer(u)
    steps = input()
    for s in steps:
        if s == 'U':
            if layer == depth - 1:
                continue
            k = u // 2 ** (layer + 1) // 2
            layer += 1
            u = 2 ** (layer + 1) * k + 2 ** layer
        elif layer == 0:
            continue
        elif s == 'R':
            k = u // 2 ** (layer + 1) * 2 + 1
            layer -= 1
            u = 2 ** (layer + 1) * k + 2 ** layer
        elif s == 'L':
            k = u // 2 ** (layer + 1) * 2
            layer -= 1
            u = 2 ** (layer + 1) * k + 2 ** layer
    print(u)
