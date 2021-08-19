(n, m) = list(map(int, input().split()))
arr = list(map(int, input().split()))
up = [i for i in range(n)]
down = [i for i in range(n)]
for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        up[i] = up[i - 1]
    if arr[i - 1] >= arr[i]:
        down[i] = down[i - 1]
all_res = []
seg = list(tuple((list(map(int, input().split())) for _ in range(m))))
for (l, r) in seg:
    if l - 1 >= up[down[r - 1]]:
        all_res.append('Yes')
    else:
        all_res.append('No')
print('\n'.join(all_res))
