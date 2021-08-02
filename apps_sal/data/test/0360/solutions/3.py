n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
k = int(input()) - 1
cnt = 0
for el in arr:
    if el[1] <= k:
        cnt += 1
print(n - cnt)
