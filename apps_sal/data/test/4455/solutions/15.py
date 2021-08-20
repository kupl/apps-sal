(n, k) = map(int, input().split())
m = list(map(int, input().split()))
new_m = [(m[i], i) for i in range(n)]
new_m.sort()
ans = [0 for i in range(n)]
last = -1
for i in range(1, len(new_m)):
    if new_m[i][0] == new_m[i - 1][0]:
        ans[new_m[i][1]] = ans[new_m[i - 1][1]]
    else:
        ans[new_m[i][1]] = i
for i in range(k):
    (a, b) = map(int, input().split())
    if m[a - 1] > m[b - 1]:
        ans[a - 1] -= 1
    elif m[a - 1] != m[b - 1]:
        ans[b - 1] -= 1
print(*ans)
