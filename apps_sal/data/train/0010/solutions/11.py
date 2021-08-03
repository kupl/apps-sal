import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = [p[0]]
    for i in range(n - 2):
        if (p[i] - p[i + 1]) * (p[i + 1] - p[i + 2]) < 0:
            ans.append(p[i + 1])
    ans.append(p[-1])
    print(len(ans))
    print(*ans)
