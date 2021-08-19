def __starting_point():
    n = int(input())
    A = [int(num) for num in input().split(' ')]
    opponent_votes = sum(A)
    min_k = max(A)
    while sum([min_k - a for a in A]) <= opponent_votes:
        min_k += 1
    print(min_k)


__starting_point()
