(n, k) = map(int, input().split())
A = list(map(int, input().split()))
A = [(a, i) for (i, a) in enumerate(A)]
A.sort(key=lambda x: x[0])
A.reverse()
left = [-1] * n
for i in range(1, n):
    left[i] = i - 1
right = [-1] * n
for i in range(n - 1):
    right[i] = i + 1
vis = [0] * n
join = [0] * n
jo = 1
for i in range(n):
    if not vis[A[i][1]]:
        cur = A[i][1]
        vis[cur] = 1
        join[cur] = jo
        if left[cur] != -1:
            right[left[cur]] = right[cur]
        if right[cur] != -1:
            left[right[cur]] = left[cur]
        for j in range(k):
            cur = left[cur]
            if cur == -1:
                break
            vis[cur] = 1
            join[cur] = jo
            if left[cur] != -1:
                right[left[cur]] = right[cur]
            if right[cur] != -1:
                left[right[cur]] = left[cur]
        cur = A[i][1]
        for j in range(k):
            cur = right[cur]
            if cur == -1:
                break
            vis[cur] = 1
            join[cur] = jo
            if left[cur] != -1:
                right[left[cur]] = right[cur]
            if right[cur] != -1:
                left[right[cur]] = left[cur]
        jo = 1 if jo == 2 else 2
print(*join, sep='')
