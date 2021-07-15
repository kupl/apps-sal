n = int(input())
t = list(map(int, input().split()))
n = len(t)
t.sort()
ans = 1
s = t[0]
for i in range(1,n):
    if s <= t[i]:
        ans += 1
        s += t[i]
print(ans)


