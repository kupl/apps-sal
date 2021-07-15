from collections import Counter
t = int(input())
inf = 10**18
for _ in range(t):
    n = int(input())
    s = input()
    ans = [inf, 0, 0]
    cnt = Counter({(0, 0): 1})
    x, y = 0, 0

    for i, c in enumerate(s, start=1):
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y -= 1
        else:
            y += 1
        if (x, y) in cnt and i - cnt[(x, y)] < ans[0]:
            ans[0] = i - cnt[(x, y)]
            ans[1], ans[2] = cnt[(x, y)], i
        cnt[(x, y)] = i+1

    if ans[0] < inf:
        print(ans[1], ans[2])
    else:
        print(-1)

