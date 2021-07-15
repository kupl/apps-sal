import sys
n, m = map(int, input().split())
if m > n:
    print(n + 1)
    curr = (0, 1)
    while curr[0] <= n:
        print(curr[0],curr[1])
        curr = (curr[0] + 1, curr[1] + 1)
    return
if m == n:
    print(n + 1)
    curr = (0, n)
    while curr[0] <= n:
        print(curr[0],curr[1])
        curr = (curr[0] + 1, curr[1] - 1)
    return
print(m + 1)
curr = (1, 0)
while curr[1] <= m:
    print(curr[0],curr[1])
    curr = (curr[0] + 1, curr[1] + 1)
