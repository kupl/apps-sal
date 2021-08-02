n, k = map(int, input().split())
L = list(map(int, input().split()))
label = 0
ans = 1
for i in range(1, n):
    if L[i] == L[i - 1]:
        label = i
    cur = i - label + 1
    if cur > ans:
        ans = cur
print(ans)
