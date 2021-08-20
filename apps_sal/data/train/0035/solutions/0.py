import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    e = list(map(int, input().split()))
    e.sort()
    ans = 0
    val = 0
    g = 0
    for i in range(0, N):
        g += 1
        val = e[i]
        if g >= val:
            ans += 1
            g = 0
            val = 0
    print(ans)
