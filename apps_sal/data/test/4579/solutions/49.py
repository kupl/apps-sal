def main():
    n = int(input())
    seen = []
    for i in range(n):
        item = input()
        seen.append(item)
    return len(list(set(seen)))


def __starting_point():
    print((main()))

__starting_point()
