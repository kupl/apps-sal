import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
diff = [0 for i in range(n)]
for i in range(1, n):
    diff[i] = a[i] - a[i - 1]
S = 0
for i in range(1, n):
    if diff[i] >= 0:
        S += diff[i]
first = a[0]
ans = []
res = S + first
ans.append((res + 1) // 2)
Q = int(input())
for _ in range(Q):
    (l, r, x) = map(int, input().split())
    l = l - 1
    r = r - 1
    if l == 0:
        first += x
    else:
        if diff[l] >= 0:
            S -= diff[l]
        diff[l] += x
        if diff[l] >= 0:
            S += diff[l]
    if r + 1 < n:
        if diff[r + 1] >= 0:
            S -= diff[r + 1]
        diff[r + 1] -= x
        if diff[r + 1] >= 0:
            S += diff[r + 1]
    res = S + first
    ans.append((res + 1) // 2)
for a in ans:
    print(a)
