import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = tuple(map(int, input().split()))

    b = []
    box = [0] * (N + 1)
    for i, r in zip(reversed(list(range(1, N + 1))), a[::-1]):
        total_r = sum(box[j] for j in range(i, N + 1, i)) % 2
        if r == 0 and total_r == 1:
            box[i] = 1
            b.append(i)
        elif r == 1 and total_r == 0:
            box[i] = 1
            b.append(i)

    M = len(b)
    if M == 0:
        print((0))
    else:
        print(M)
        print((" ".join(map(str, b))))


def __starting_point():
    main()


__starting_point()
