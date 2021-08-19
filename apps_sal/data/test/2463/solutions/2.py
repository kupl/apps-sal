def read_line():
    return list(map(int, input().split()))


n = int(input())
l = sorted(read_line())
ans = [0] * n
idx = 0
for i in range(1, n, 2):
    ans[i] = l[idx]
    idx += 1
for i in range(0, n, 2):
    ans[i] = l[idx]
    idx += 1
v = 0
for i in range(1, n - 1):
    if ans[i - 1] > ans[i] and ans[i] < ans[i + 1]:
        v += 1
print(v)
print(' '.join(map(str, ans)))
