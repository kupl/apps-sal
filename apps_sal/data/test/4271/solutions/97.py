N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


def main():
    score = 0
    for i in range(N):
        score += B[A[i] - 1]
        if A[i] == A[i - 1] + 1 and i >= 1:
            score += C[A[i - 1] - 1]

    return score


print(main())
