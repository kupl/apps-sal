from heapq import heapify, heappushpop
import sys
sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    H = [a for a in A[:N]]
    heapify(H)
    B[0] = sum(A[:N])
    for i in range(N):
        x = heappushpop(H, A[N + i])
        B[i + 1] = B[i] + A[N + i] - x
    H = [-a for a in A[2 * N:]]
    heapify(H)
    C[0] = sum(A[2 * N:])
    for i in range(N):
        x = -heappushpop(H, -A[2 * N - i - 1])
        C[i + 1] = C[i] + A[2 * N - i - 1] - x
    print(max((b - c for (b, c) in zip(B, C[::-1]))))


def __starting_point():
    main()


__starting_point()
