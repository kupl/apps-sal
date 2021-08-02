n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
k = 1
for i in a:
    if i >= k:
        ans += 1
        k += 1
print(ans)
