n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = sum(a)
a = [i if i <= x else x for i in a]
for i in range(n-1):
    if a[i]+a[i+1] > x:
        a[i+1] = x-a[i]
print(ans-sum(a))
