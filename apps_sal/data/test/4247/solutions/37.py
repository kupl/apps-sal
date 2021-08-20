n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n - 2):
    if p[i] < p[i + 1] and p[i + 1] < p[i + 2] or (p[i] > p[i + 1] and p[i + 1] > p[i + 2]):
        cnt += 1
print(cnt)
