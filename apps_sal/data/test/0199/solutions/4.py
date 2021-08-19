(n, s) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
d = sum(a)
if d >= s:
    r = d - s
    ans = min(r // n, a[0])
else:
    ans = -1
print(ans)
