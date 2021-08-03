n, m = list(map(int, input().split()))
ans = []
for i in range(1, m + 1):
    ans.append(i)
ans = set(ans)
for i in range(n):
    a = list(map(int, input().split()))
    del a[0]
    a = set(a)
    ans = ans & a
print((len(ans)))
