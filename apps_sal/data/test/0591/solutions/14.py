def main():
    with open("input.txt", "r") as f:
        n, k, = list(map(int, f.readline().split()))
        l = [-1] + list(map(int, f.readline().split()))
    idx = sorted(list(range(1, n + 1)), key=l.__getitem__, reverse=True)[:k]
    with open("output.txt", "w") as f:
        f.writelines((str(l[idx[-1]]), '\n', ' '.join(map(str, idx))))


def __starting_point():
    main()

__starting_point()
