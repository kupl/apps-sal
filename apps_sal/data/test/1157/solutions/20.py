n = int(input())
arr = [int(s) for s in input().split()]
ans = [0, 0]
last = [0, 0]
now = 0
for i in arr:
    if i < 0:
        now = 1 if now == 0 else 0
    last[now] += 1
ans[0] += last[0]
ans[1] += last[1]
for i in range(1, n):
    if arr[i - 1] < 0:
        (last[0], last[1]) = (last[1], last[0])
    last[0] -= 1
    ans[0] += last[0]
    ans[1] += last[1]
print(ans[1], ans[0])
