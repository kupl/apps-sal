def solve():
    (n, m) = map(int, input().split())
    lastline = []
    lastcol = []
    for _ in range(n):
        s = input()
        if _ + 1 < n:
            lastcol.append(s[-1])
        else:
            lastline = list(s)[:-1]
    print(lastcol.count('R') + lastline.count('D'))


t = int(input())
for _ in range(t):
    solve()
