n = int(input())
h = list(map(int, input().split()))
cnt = 0
max = 0
for i in range(n):
    if max <= h[i]:
        cnt += 1
        max = h[i]
print(cnt)
