import collections


def game(n, A):
    if N % 2 == 0:
        ans = 'Second'
        B = collections.Counter(A)
        for i in list(B.values()):
            if i % 2 != 0:
                ans = 'First'
    else:
        ans = 'Second'
    return ans


T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    score = game(N, A)
    print(score)
