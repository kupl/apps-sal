
def solve():
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    a_line = []
    for i, i_cnt in enumerate(a):
        color = i + 1
        for j in range(i_cnt):
            a_line.append(color)
    ans = [[''] * w for _ in range(h)]
    cur = 0
    for i in range(h):
        for j in range(w):
            ans[i][j] = str(a_line[cur])
            cur += 1
    for i in range(h):
        print(' '.join(ans[i] if i % 2 == 0 else reversed(ans[i])))


solve()
