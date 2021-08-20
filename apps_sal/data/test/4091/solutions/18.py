(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = sorted(a)[-k:]
print(sum(b))
used = [0 for i in range(n)]
for elem in b:
    for i in range(n):
        if a[i] == elem and used[i] == 0:
            used[i] = 1
            break
last = 0
count = 0
ans = []
for i in range(n):
    if used[i]:
        ans.append(i - last + 1)
        last = i + 1
        count += 1
    if count == k:
        ans.pop()
        ans.append(n - sum(ans))
print(*ans)
