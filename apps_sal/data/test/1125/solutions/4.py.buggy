import sys
N = int(input())
A = list(map(int, input().split()))
ALL = 0
for a in A:
    ALL ^= a

if ALL == 0:
    print(0)
    return

ALL ^= A[0] ^ A[1]

K = A[0] + A[1]
L = []

for i in range(40, -1, -1):
    if (1 << i) & ALL:
        L.append(1)
        K -= (1 << i)
    else:
        if K >= 2 * (1 << i):
            L.append(2)
            K -= 1 << (i + 1)
        else:
            L.append(0)

if K != 0:
    print(-1)
    return

ans = 0
for i in range(41):
    if L[i] == 2:
        ans += 1 << (40 - i)

if ans >= A[0]:
    print(-1)
    return

for i in range(41):
    if L[i] == 1:
        if ans + (1 << (40 - i)) < A[0]:
            ans += 1 << (40 - i)

if ans == 0:
    print(-1)
    return

print(A[0] - ans)
