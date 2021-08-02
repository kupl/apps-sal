n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
curr = 0
ans = 0
while curr < len(a):
    if k >= a[curr] / 2:
        k = max(k, a[curr])
        curr += 1
    else:
        ans += 1
        k *= 2

print(ans)
