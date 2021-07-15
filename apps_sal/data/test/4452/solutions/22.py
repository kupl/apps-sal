import sys
readline = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = readline().rstrip()
    ans = []
    for i, c in zip(list(range(100)), reversed(n)):
        if c != '0':
            ans.append(c + '0'*i)
    print(len(ans))
    print(*ans)

