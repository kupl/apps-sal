import sys
input = sys.stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        x = a[i]
        c = 1
        while not (i + 1) == x:
            x = a[x - 1]
            c += 1
        ans.append(c)
    print(*ans)
