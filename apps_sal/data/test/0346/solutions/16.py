import sys


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    auction_questions = set(map(int, input().split()))

    regular_a = [a[i] for i in range(len(a)) if (i + 1) not in auction_questions]
    auction_a = [a[i] for i in range(len(a)) if (i + 1) in auction_questions]

    total_points = sum(regular_a)
    auction_a.sort(reverse=True)
    for a in auction_a:
        if a < total_points:
            total_points += total_points
        else:
            total_points += a
    print(total_points)


def __starting_point():
    main()

__starting_point()
