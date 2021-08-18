

def solve(N):
    answer = 0
    for i in range(1, N + 1):
        mprime = N // i
        answer += i * (mprime * (mprime + 1)) // 2
    return answer


def main():
    N = int(input())
    answer = solve(N)
    print(answer)


def __starting_point():
    main()


__starting_point()
