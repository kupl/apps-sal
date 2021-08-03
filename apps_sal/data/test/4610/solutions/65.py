from collections import Counter


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    unchange = sum(tuple[1] for tuple in Counter(A).most_common(K))
    print(N - unchange)


main()
