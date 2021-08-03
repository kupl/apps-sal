from collections import defaultdict


def main():
    n = int(input())
    a = map(int, input().split())
    count = defaultdict(lambda: 0)
    for x in a:
        count[x] += 1
    print(max(count.values()))


main()
