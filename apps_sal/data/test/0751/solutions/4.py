n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 1
avt = m
i = 0
while i < n:
    if a[i] <= avt:
        avt -= a[i]
        i+=1
    else:
        ans += 1
        avt = m
print(ans)
