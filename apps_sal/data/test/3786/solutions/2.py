# python3


def main():
    n = int(input())
    parent = tuple(int(x) - 1 for x in input().split())

    depth = [0]
    for v in range(n - 1):
        depth.append(depth[parent[v]] + 1)

    parity = [0] * n
    for d in depth:
        parity[d] ^= 1

    print(sum(parity))


main()
