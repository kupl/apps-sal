

def solve(A: "List[int]"):
    return ["win", "bust"][sum(A) >= 22]


def main():
    A = list(map(int, input().split()))
    answer = solve(A)
    print(answer)


def __starting_point():
    main()


__starting_point()
