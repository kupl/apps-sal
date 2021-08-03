import sys

N = int(input())
fixed = []
up_only = []
down_only = []
up_set = set()
down_set = set()

for i in range(N):
    A, B = map(int, input().split())
    if A == -1 and B == -1:
        continue
    elif A in up_set or B in down_set or A == 2 * N or B == 1:
        print("No")
        return
    elif A == -1:
        down_only.append((A, B))
        down_set.add(B)
    elif B == -1:
        up_only.append((A, B))
        up_set.add(A)
    else:
        fixed.append((A, B))
        down_set.add(B)
        up_set.add(A)

dp = [-1] * (2 * N + 1)

for a, b in fixed:
    if a >= b:
        print("No")
        return
    else:
        c = b - a
        for i in range(a, b):
            if dp[i] == -1:
                dp[i] = c
            elif dp[i] != c:
                print("No")
                return

down_only.sort(reverse=True)
up_only.sort()

for na, b in down_only:
    if dp[b] != -1:
        na = b - dp[b]
        if na < 1 or na in up_set:
            print("No")
            return
        else:
            up_set.add(na)
        for i in range(na, b):
            if dp[i] == -1:
                dp[i] = dp[b]
            elif dp[i] != dp[b]:
                print("No")
                return
for a, nb in up_only:
    if dp[a] != -1:
        nb = a + dp[a]
        if nb > 2 * N or nb in down_set:
            print("No")
            return
        else:
            down_set.add(nb)
        for i in range(a, nb):
            if dp[i] == -1:
                dp[i] = dp[a]
            elif dp[i] != dp[a]:
                print("No")
                return

print("Yes")
