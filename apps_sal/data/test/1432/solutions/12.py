n = int(input())
a = list(map(int, input().split()))
l = []
ans = sum(a[0::2]) - sum(a[1::2])
l.append(ans)
for i in range(n - 1):
    l.append(a[i] * 2 - l[i])
print(*l)
