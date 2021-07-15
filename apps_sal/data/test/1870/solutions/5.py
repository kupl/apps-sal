n, c = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 1
for i in range(1, len(t)):
    if t[i] - t[i - 1] <= c:
        ans += 1
    else:
        ans = 1
print(ans)
