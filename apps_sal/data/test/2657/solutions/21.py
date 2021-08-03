n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

num = a[0]
tmp = a[1]
for j in range(1, n):
    if abs(tmp - num / 2) >= abs(a[j] - num / 2):
        tmp = a[j]
    else:
        break
ans = [num, tmp]
print(*ans)
