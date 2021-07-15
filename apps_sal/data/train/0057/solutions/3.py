def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = []
    for i in a:
        while len(q) >= 2 and ((q[-2] < q[-1] and q[-1] > i) or (q[-2] > q[-1] and q[-1] < i)):
            q.pop(-1)
        q.append(i)
    for i in range(len(q) - 1):
        if q[i] > q[i + 1]:
            print('NO')
            return
    print('YES')

t = int(input())
for _ in range(t):
    solve()
