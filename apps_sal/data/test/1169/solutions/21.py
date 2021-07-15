n,m = map(int, input().split())
if n > 1 and m >= n/2:
    ans1 = 0
else:
    if n > 1:
        ans1 = n - m*2
    else:
        ans1 = 1
k = 1
while k*(k-1)//2 < m:
    k += 1
if m > 0:
    ans2 = n - k
else:
    ans2 = n
print(ans1, ans2)
