def is_nomal_case(A):
    A.sort()
    for i in range(0, len(A), 2):
        if A[i] != A[i + 1]:
            return True
    return False


def __starting_point():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        if N % 2:
            print('Second')
        elif not is_nomal_case(A):
            print('Second')
        else:
            print('First')


__starting_point()
