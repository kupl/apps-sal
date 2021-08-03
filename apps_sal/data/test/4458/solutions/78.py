n = int(input())
p = list(map(int, input().split()))

min = p[0]
cnt = 0
for i in range(n):
    if min >= p[i]:
        cnt += 1
        min = p[i]
print(cnt)
