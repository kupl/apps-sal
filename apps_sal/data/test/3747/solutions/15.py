from collections import deque
from collections import Counter


def main():
    from sys import stdin
    lines = deque(line.strip() for line in stdin.readlines())
    counts = Counter(lines[0])
    bulbasaur = Counter("Bulbasaur")
    minCount = len(lines[0])
    for letter, count in list(bulbasaur.items()):
        minCount = min(minCount, counts[letter] // count)
    print(minCount)


def __starting_point():
    main()


__starting_point()
