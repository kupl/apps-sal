n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = True
for i in range(n):
    if a[i] != 0:
        ans += abs(a[i]) - 1
        a[i] /= abs(a[i])
    else:
        a[i] = 1
        ans += 1
        flag = False
if flag and a.count(-1) % 2 != 0:
    ans += 2
print(ans)
