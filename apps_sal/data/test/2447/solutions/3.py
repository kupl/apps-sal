import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().rstrip()
    n = len(s)
    x = s.count("1")
    op1 = [n] * n
    cnt = 0
    ans = n
    for i in range(n):
        if s[i] == "1":
            cnt += 1
        op1[i] = (i + 1) - cnt + x - cnt
        ans = min(ans, op1[i], n - op1[i])
    print(ans)
