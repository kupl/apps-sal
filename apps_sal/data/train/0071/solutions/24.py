# Lack of emotion causes lack of progress and lack of motivation. Tony Robbins

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    ans = 0
    for x in a:
        s += x
        ans = min(ans, s)
    print(-ans)
