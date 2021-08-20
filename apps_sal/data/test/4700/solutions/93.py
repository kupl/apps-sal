(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = [1] * n
for i in range(m):
    (a, b) = list(map(int, input().split()))
    if l[a - 1] < l[b - 1]:
        ans[a - 1] = 0
    elif l[a - 1] > l[b - 1]:
        ans[b - 1] = 0
    else:
        ans[a - 1] = 0
        ans[b - 1] = 0
print(sum(ans))
