
url = "https://atcoder.jp//contests/abc160/tasks/abc160_c"

import itertools


def main():
    n, m , X = list(map(int, input().split()))
    books = []
    ans = -1
    for _ in range(n):
        books.append(list(map(int, input().split())))
    for i in range(n):
        for row in itertools.combinations(list(range(0, n)), i+1):
            cost = 0
            rikai = [0] * m
            for idx in row:
                cost += books[idx][0]
                for idx2 in range(1, len(books[idx])):
                    rikai[idx2 - 1] += books[idx][idx2]
                if len(list([x for x in rikai if x >= X])) == len(rikai):
                    ans = min(ans, cost) if ans != -1 else cost
    print(ans)








def __starting_point():
    main()

__starting_point()
