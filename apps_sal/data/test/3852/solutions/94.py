# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    mxi = -1
    mxa = 0
    for i, a in enumerate(A):
        if abs(a) >= abs(mxa):
            mxa = a
            mxi = i
    ans = []
    for i in range(N):
        if A[i] * mxa < 0:
            ans.append((mxi + 1, i + 1))
            A[i] += mxa
    if mxa > 0:
        for i in range(1, N):
            if A[i] < A[i - 1]:
                ans.append((i, i + 1))
                A[i] += A[i - 1]
    else:
        for i in range(N - 2, -1, -1):
            if A[i] > A[i + 1]:
                ans.append((i + 2, i + 1))
                A[i] += A[i + 1]
    print((len(ans)))
    for a in ans:
        print((*a))

def __starting_point():
    input = sys.stdin.readline
    N = int(input())
    *A, = list(map(int, input().split()))
    main(N, A)

__starting_point()
