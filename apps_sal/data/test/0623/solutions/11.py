def read_input():
    a1, a2 = list(map(int, input().strip().split()))
    return a1, a2


def solution(a1, a2):
    ans = 0
    while a1 > 0 and a2 > 0:
        if a1 <= 1 and a2 <= 1:
            break
        if a1 <= a2:
            a1 += 1
            a2 -= 2
        else:
            a2 += 1
            a1 -= 2

        ans += 1
    return ans


def __starting_point():
    a1, a2 = read_input()
    print(solution(a1, a2))

__starting_point()
