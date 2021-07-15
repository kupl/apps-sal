n = int(input())
a = list(map(int, input().split()))
ans = 0
k = 0
for i in range(n):
    if i == a[i]:
        ans += 1
    elif a[a[i]] == i and k != 2:
        ans += 2
        if k == 1:
            ans -= 1
        k = 2
    elif k == 0:
        ans += 1
        k = 1
print(ans)
