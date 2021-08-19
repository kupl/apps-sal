(n, m) = list(map(int, input().split()))
al = list((list(map(int, input().split())) for _ in range(n)))
cl = list((list(map(int, input().split())) for _ in range(m)))
for a in al:
    ans = 1001001001
    no = 0
    for i in range(m):
        dis = abs(a[0] - cl[i][0]) + abs(a[1] - cl[i][1])
        if dis < ans:
            ans = dis
            no = i
    print(no + 1)
