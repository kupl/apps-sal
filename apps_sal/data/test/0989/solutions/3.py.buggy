import sys
from collections import Counter
input = sys.stdin.readline

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

S = sorted(set(A))

if len(S) == 1:
    print(0)
    return

MIN0 = 0
MIN1 = 1
MAX0 = -1
MAX1 = -2

C = Counter(A)

while k and S[MIN0] != S[MAX0]:

    if C[S[MIN0]] <= C[S[MAX0]] and k >= C[S[MIN0]]:

        if k >= (S[MIN1] - S[MIN0]) * C[S[MIN0]]:

            k -= (S[MIN1] - S[MIN0]) * C[S[MIN0]]
            C[S[MIN1]] += C[S[MIN0]]
            del(C[S[MIN0]])
            MIN0 += 1
            MIN1 += 1

        else:
            print(S[MAX0] - (S[MIN0] + k // C[S[MIN0]]))
            return

    elif C[S[MAX0]] <= C[S[MIN0]] and k >= C[S[MAX0]]:

        if k >= (S[MAX0] - S[MAX1]) * C[S[MAX0]]:

            k -= (S[MAX0] - S[MAX1]) * C[S[MAX0]]
            C[S[MAX1]] += C[S[MAX0]]
            del(C[S[MAX0]])
            MAX0 -= 1
            MAX1 -= 1

        else:
            print((S[MAX0] - k // C[S[MAX0]]) - S[MIN0])
            return

    else:
        break

print(S[MAX0] - S[MIN0])
