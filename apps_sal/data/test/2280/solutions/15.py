from sys import stdin
c = int(stdin.readline().strip())
for i in range(c):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    s.sort()
    l = min(s[-1], s[-2])
    ans = min(l - 1, n - 2)
    print(ans)
