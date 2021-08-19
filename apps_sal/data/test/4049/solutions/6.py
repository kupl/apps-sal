from sys import stdin, stdout


def find(A, B, N):
    X = min(A[0], B[1])
    Y = min(A[1], B[2])
    Z = min(A[2], B[0])
    P = min(A[0], B[2] + B[0])
    Q = min(A[1], B[1] + B[0])
    R = min(A[2], B[2] + B[1])
    return (N - (P + Q + R), X + Y + Z)


def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    print(' '.join(map(str, find(A, B, N))))


main()
