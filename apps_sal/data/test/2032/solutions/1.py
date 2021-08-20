import sys
input = sys.stdin.readline
(n, m, k) = map(int, input().split())
cas = [list(map(int, input().split())) for i in range(n)]
pot = [list(map(int, input().split())) for i in range(m)]
timing = [i for i in range(n)]
for i in range(m):
    (a, b) = pot[i]
    a -= 1
    b -= 1
    if a > b:
        (a, b) = (b, a)
    timing[a] = max(b, timing[a])
time = [[] for i in range(n)]
for i in range(n):
    time[timing[i]].append(cas[i][2])
for i in range(n):
    time[timing[i]].sort(reverse=True)
memo = {}
memo[k] = 0
for i in range(n):
    (a, add_, c) = cas[i]
    memo2 = {}
    for j in memo:
        if j >= a:
            memo2[j + add_] = memo[j]
    for num in time[i]:
        tmp = memo2.copy()
        for j in tmp:
            if j - 1 not in memo2:
                memo2[j - 1] = tmp[j] + num
            else:
                memo2[j - 1] = max(tmp[j - 1], tmp[j] + num)
    memo = memo2.copy()
ans = -1
for i in memo:
    ans = max(ans, memo[i])
print(ans)
