n = int(input())
a = list(map(int, input().split()))
ans = 0
flg = False
for i in range(n):
    if flg:
        flg = False
        continue
    if a[i] == i + 1:
        if i < n - 1 and a[i + 1] == i + 2:
            ans += 1
            flg = True
        else:
            ans += 1
print(ans)
