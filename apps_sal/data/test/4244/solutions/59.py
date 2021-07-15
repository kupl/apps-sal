n = int(input())
l = list(map(int, input().split()))

cnt_m = float('inf')
for i in range(1, 101):
    cnt = 0
    for j in range(n):
        cnt += (l[j] - i) ** 2
    cnt_m = min(cnt_m, cnt)

print(cnt_m)
