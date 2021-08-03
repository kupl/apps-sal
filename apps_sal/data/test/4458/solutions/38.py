n = int(input())
p = list(map(int, input().split()))

mini = float("inf")
cnt = 0
for i in range(n):
    if p[i] <= mini:
        cnt += 1
        mini = p[i]
print(cnt)
