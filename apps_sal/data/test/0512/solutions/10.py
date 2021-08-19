INF = float('inf')


def no():
    print('No')
    return


N = int(input())
ms = 0
arr = []
L = []
R = []
seen = [False] * (2 * N)
for i in range(N):
    (A, B) = map(int, input().split())
    if A == -1 and B == -1:
        ms += 1
    elif A == -1:
        R.append(B - 1)
    elif B == -1:
        L.append(A - 1)
    else:
        arr.append((A - 1, B - 1))
    if A != -1:
        if seen[A - 1]:
            no()
        seen[A - 1] ^= 1
    if B != -1:
        if seen[B - 1]:
            no()
        seen[B - 1] ^= 1
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        (l1, r1) = arr[i]
        (l2, r2) = arr[j]
        if l1 <= l2 and l2 <= r1 and (r1 - l1 != r2 - l2):
            no()
dp = [INF] * (2 * N + 1)
dp[0] = 0
for k in range(1, 2 * N + 1):
    if k % 2:
        continue
    for j in range(k - 1):
        if dp[j] == INF:
            continue
        M = 0
        for l in range(j, (j + k) // 2):
            if (l, l + (k - j) // 2) in arr or l in L or l + (k - j) // 2 in R:
                continue
            else:
                M += 1
        if M <= ms:
            dp[k] = min(dp[k], dp[j] + M)
print('Yes' if dp[2 * N] == ms else 'No')
