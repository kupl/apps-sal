import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    x0, x1, x2, x3 = int(s[0][1]), int(s[1][0]), int(s[-1][-2]), int(s[-2][-1])
    ans = []
    if x0 == 1:
        ans.append((1, 2))
    if x1 == 1:
        ans.append((2, 1))
    if x2 == 0:
        ans.append((n, n - 1))
    if x3 == 0:
        ans.append((n - 1, n))
    if len(ans) <= 2:
        print(len(ans))
        for i in ans:
            print(*i)
        continue
    ans = []
    if x0 == 0:
        ans.append((1, 2))
    if x1 == 0:
        ans.append((2, 1))
    if x2 == 1:
        ans.append((n, n - 1))
    if x3 == 1:
        ans.append((n - 1, n))
    print(len(ans))
    for i in ans:
        print(*i)
