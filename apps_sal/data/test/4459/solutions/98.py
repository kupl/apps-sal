from collections import Counter
from itertools import starmap


def main():
    N = input()
    A = list(map(int, input().split()))
    count = Counter(A)

    def remove(x, y):
        return y - x if y >= x else y
    ans = sum(starmap(remove, count.items()))
    print(ans)


main()
