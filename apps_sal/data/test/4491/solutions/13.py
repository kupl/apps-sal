n = int(input())
l = [list(map(int, input().split())) for _ in range(2)]
r1 = [sum(l[0][:i + 1]) for i in range(n)]
r2 = [sum(l[1][i:]) for i in range(n)]
max_cnt = 0
for i in range(n):
    cnt = r1[i] + r2[i]
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
