from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ss = [input().rstrip() for _ in range(N)]

C = Counter(Ss)

ans1 = ""
only_used = ""
for S in Ss:
    Is = S[::-1]
    if S != Is:
        if Is in C and C[Is] > 0:
            C[Is] -= 1
            C[S] -= 1
            ans1 += S
    else:
        if S in C and C[Is] > 1:
            C[S] -= 2
            ans1 += S
        elif S in C and C[Is] == 1:
            C[S] = 0
            only_used = S

ans = ans1 + only_used + ans1[::-1]
print(len(ans))
print(ans)
