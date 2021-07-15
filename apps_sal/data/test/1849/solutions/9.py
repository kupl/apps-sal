
n = int(input())

mod = 998244353

ans = []

for i in range(n,0,-1):

    if i == n:
        ans.append(10)
    elif i == n-1:
        ans.append(180)
    else:

        now = 10 * 2 * 9 * pow(10,n-i-1,mod)
        #print (now)
        now += 10 * (n-i-1) * 81 * pow(10,n-i-2,mod)
        ans.append(now % mod)

ans.reverse()
print(*ans)

