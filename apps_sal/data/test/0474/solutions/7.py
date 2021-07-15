n = int(input())
a = list(map(int, input().split()))
c = max(a)
le = 0
ans = -1
for i in range(n):
    if c == a[i]:
        le += 1
    else:
        le = 0
    ans = max(ans, le)
print(ans)
