n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    p, x = px[i][0], px[i][1]
    p -= 1
    cnt = 0
    for j in range(n):
        if p == j:
            cnt += x
        else :
            cnt += t[j]
    print(cnt)

