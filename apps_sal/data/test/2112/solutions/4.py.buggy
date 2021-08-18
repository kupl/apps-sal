import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
x, k, y = list(map(int, input().split()))
B = list(map(int, input().split()))
A = list(map(int, input().split()))

inda = 0
for b in B:
    if b == A[inda]:
        inda += 1
    if inda == len(A):
        break

if inda != len(A):
    print(-1)
    return

B += [0]
A = set(A) | {0}

ONE = 0
TWO = 0
C = []
ANS = 0

for b in B:
    if not(b in A):
        C.append(b)

    else:
        ONE = TWO
        TWO = b

        MAX = max(ONE, TWO)

        L = len(C)
        ST = 0
        for c in C:
            if c > MAX:
                ST += 1

        if ST > 0 and L < k:
            print(-1)
            return

        else:
            if ST > 0:
                COST = x
                rest = L - k
                COST += min((rest // k) * x + (rest % k) * y, rest * y)
                ANS += COST
                C = []
            else:
                COST = min((L // k) * x + (L % k) * y, L * y)
                ANS += COST
                C = []


print(ANS)
