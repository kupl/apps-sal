def prime_table(n):
    arr = [True] * (n + 1)
    arr[0], arr[1] = False, False
    for i in range(2, N + 1):
        if not arr[i]:
            continue
        j = 2 * i
        while j <= n:
            arr[j] = False
            j += i
    return arr


N = 10**5
pt = prime_table(N)
cum = [0] * (N + 1)
for i in range(1, N + 1, 2):
    if pt[i] and pt[(i + 1) // 2]:
        cum[i] = 1
for i in range(1, N + 1):
    cum[i] += cum[i - 1]
Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(cum[r] - cum[l - 1])
print(*ans, sep="\n")
