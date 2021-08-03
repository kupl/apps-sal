import sys
n = int(input())
a = input().split()
arr = [int(_) for _ in a]
cnt = [0 for _ in range(n + 1)]
must = [False for _ in range(n + 1)]
for x in arr:
    cnt[x] += 1

que = []
for i in range(1, n + 1):
    if cnt[i] == 0:
        que.append(i)

cur = 0
for i in range(n):
    x = arr[i]
    if cnt[x] > 1:
        if must[x] or que[cur] < x:
            cnt[x] -= 1
            arr[i] = que[cur]
            cur += 1
        else:
            must[x] = True


print(cur)
for x in arr:
    print(x, end=' ')
