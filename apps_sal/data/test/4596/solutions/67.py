import sys


def solve(N, A):
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 > 0:
                print(count)
                return
            A[i] = A[i] / 2
        count += 1
    

def __starting_point():
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)

__starting_point()
