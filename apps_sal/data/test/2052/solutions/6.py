inf = 2000000000
w, l = list(map(int, input().split()))
aa = input().split()

a = [0 for i in range(w)]
dp = [0 for i in range(w+1)]
su = [0 for i in range(w+1)]

for i in range(1, w):
    a[i] = int(aa[i-1])

for i in range(1, w):
    if i <= l :
        dp[i] = a[i]
    else :
        dp[i] = min(a[i], su[i-1] - su[i-l-1])
    su[i] = su[i-1] + dp[i]
#    print(i, ' -- ', dp[i])
res = inf

for i in range(l, w):
    res = min(res, su[i] - su[i-l])

print(res)

