n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    x = str(i)
    cnt = 0
    for j in range(len(x)):
        cnt += int(x[j])
    if a <= cnt and cnt <= b:
        ans += i
print(ans)
