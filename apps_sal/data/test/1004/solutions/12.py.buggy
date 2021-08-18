import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

NOW = set()
USED = set()
ANS = [0]
for i in range(n):
    if A[i] > 0:
        if A[i] in NOW or A[i] in USED:
            print(-1)
            return
        else:
            NOW.add(A[i])
            USED.add(A[i])

    else:
        if -A[i] in NOW:
            NOW.remove(-A[i])
        else:
            print(-1)
            return
    if NOW == set():
        ANS.append(i + 1)
        USED = set()

if len(NOW) > 0:
    print(-1)
    return

print(len(ANS) - 1)
ANS2 = [ANS[i] - ANS[i - 1] for i in range(1, len(ANS))]
print(" ".join(map(str, ANS2)))
