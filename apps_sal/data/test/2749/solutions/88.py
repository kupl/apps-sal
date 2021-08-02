h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
temp = []
for i in range(n):
    for _ in range(a[i]):
        temp.append(i + 1)

ans = []
for j in range(h):
    if j % 2 == 0:
        ans.append(list(temp[j * w:(j + 1) * w]))
    else:
        ans.append(list(temp[(j + 1) * (w) - 1:j * w - 1:-1]))


for k in ans:
    ans2 = [str(v) for v in k]
    print(" ".join(ans2))
