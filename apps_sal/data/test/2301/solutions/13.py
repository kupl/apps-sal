n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
t = n - (n - 1) // 2
ans = [0 for _ in range(n)]
for i in range(t):
    x = i * 2
    if x == n:
        x -= 1
    ans[x] = arr[i]
cur = 1
cur2 = n - 2
if n % 2 == 0:
    cur2 -= 1
for i in range(t, n):
    if ans[cur - 1] > arr[i] < ans[cur + 1]:
        ans[cur] = arr[i]
        cur += 2
    else:
        ans[cur2] = arr[i]
        cur2 -= 2
answer = sum((ans[i - 1] > ans[i] < ans[i + 1] for i in range(1, n - 1)))
print(answer)
print(*ans)
