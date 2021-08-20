from collections import Counter


def read_input():
    N = int(input())
    A = [int(i) for i in input().strip().split()]
    return A


def solution(A):
    c = Counter(A)
    ans = 0
    stop = False
    while not stop:
        stop = True
        count = 0
        for key in c:
            if c[key]:
                count += 1
                stop = False
                c[key] -= 1
        if count:
            ans += count - 1
    return ans


def __starting_point():
    A = read_input()
    print(solution(A))


__starting_point()
