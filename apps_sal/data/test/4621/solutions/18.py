(H, W) = map(int, input().split())
C = [input() for _ in range(H)]


def Wprint(x):
    return (print(x), print(x))


for c in C:
    Wprint(c)
