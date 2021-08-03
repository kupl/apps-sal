# map(int,input().split())
# int(input())
n = int(input())
a = list(map(int, input().split()))
a.sort()
cm = 0
ans = 1
i = 1
while i < n:
    if a[i] - a[cm] <= 5:
        i += 1
        ans = max(i - cm, ans)
    else:
        while cm <= i and a[i] - a[cm] > 5:
            cm += 1
print(ans)
