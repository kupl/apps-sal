

def solve(H: int):
    n = 1
    attack = 0
    while H > 1:
        attack += n
        H = H // 2
        n *= 2
    attack += n
    return attack


def main():
    H = int(input())
    answer = solve(H)
    print(answer)


def __starting_point():
    main()


__starting_point()
