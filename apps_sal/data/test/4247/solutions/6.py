n = int(input())
p = list(map(int, input().split()))
cnt = 0

for i in range(0, n - 2):
    if p[i] < p[i + 1] < p[i + 2] or p[i + 2] < p[i + 1] < p[i]:
        cnt += 1

print(cnt)
