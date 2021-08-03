n, k = input().split()
n = int(n)
k = int(k)
ans = 0
check = True
for i in range(n):
    f, t = input().split()
    f = int(f)
    t = int(t)
    if(t > k):
        j = f - (t - k)
    else:
        j = f
    if(j > ans or check):
        ans = j
        check = False
print(ans)
