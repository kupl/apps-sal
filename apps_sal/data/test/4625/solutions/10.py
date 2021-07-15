import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    s = list([ord(x)-97 for x in input().rstrip()])
    p = [n] + sorted(map(int, input().split()), reverse=True)
    ans = [0]*26

    i = 0
    for i in range(n):
        while p and p[-1] == i:
            p.pop()
        ans[s[i]] += len(p)

    print(*ans)

