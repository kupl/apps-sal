import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    S = list(map(int, input().split()))

    ans = 0
    # C = A - B
    for C in range(1, N//2):
        n = (N-1) // C
        point = 0
        for k in range(1, n):
            A = N-1 - k*C

            # Check A and B are positive integer, and S_i is not used twice.
            #
            # B = A - C and B >= 0, so A must be over C (A > C).
            #
            # If C is aliquot of N-1 (N-1 % C = 0), A is also aliquot of N-1
            # (N-1 % A = 0) because A + kC = N-1. Therefore when A is less than
            # or equal kC, the A's value is already used by kC.
            if A < C or ((N-1) % C == 0 and A <= k*C):
                break

            point += S[A] + S[k*C]
            ans = max(ans, point)

    return ans


def __starting_point():
    print((main()))

__starting_point()
