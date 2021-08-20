n = int(input())
a = sorted([int(x) for x in input().split()], reverse=True)
ans = a[0]
cnt = idx = 1
while idx < n - 1:
    for i in range(2):
        ans += a[idx]
        cnt += 1
        if cnt == n - 1:
            break
    else:
        idx += 1
        continue
    break
print(ans)
