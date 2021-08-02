n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
# arr.sort(reverse=True)

th = sum(arr) * (1 / (4 * m))
ans = 'No'
cnt = 0
for x in arr:
    if th <= x:
        cnt += 1
        if cnt == m:
            ans = 'Yes'
            break

print(ans)
