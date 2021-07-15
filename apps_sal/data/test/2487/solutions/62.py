def main():
    N = int(input())
    h = 0
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        if u > v:
            u, v = v, u
        h += u * (N + 1 - v)

    return N * (N + 1) * (N + 2) // 6 - h

print((main()))

