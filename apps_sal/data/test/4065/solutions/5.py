n = int(input())
line = list(map(int, input().split()))
ans = 1
prev_i = 0
for i in range(1, n):
    if line[i - 1] * 2 >= line[i]:
        continue
    ans = max(i - prev_i, ans)
    prev_i = i
ans = max(n - prev_i, ans)
print(ans)
