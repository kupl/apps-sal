
MOD = 10**9+7
def calc(n):
    dp = [ [0]*2 for _ in range(n) ]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(n-1):
        dp[i+1][0] = (dp[i][0] + dp[i][1])%MOD
        dp[i+1][1] = dp[i][0]%MOD
    return (dp[n-1][0] + dp[n-1][1])%MOD

def calc2(n):
    if n == 1: return 2

    dp = [ [0]*4 for _ in range(n) ]
    dp[1][0] = 1 #aa
    dp[1][1] = 1 #ab
    dp[1][2] = 1 #ba
    dp[1][3] = 1 #bb
    for i in range(1,n-1):
        dp[i+1][0] = (dp[i][0]+dp[i][2])%MOD
        dp[i+1][1] = (dp[i][0]+dp[i][2])%MOD
        dp[i+1][2] = (dp[i][1]+dp[i][3])%MOD
        dp[i+1][3] = (dp[i][1])%MOD
    # print(dp)
    return (sum(dp[n-1]))%MOD


def rev(s):
    if s == 'A': return 'B'
    else: return 'A'


# print(calc2(3))
# print(calc2(4))
# print(calc2(5))
# print(calc2(6))


n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()

if n == 2:
    print(1)
    return
if n == 3:
    print(1)
    return

# if ab == 'B':
#     aa = rev(aa)
#     ab = rev(ab)
#     ba = rev(ba)
#     bb = rev(bb)

# print('---')
# print(aa)
# print(ab)
# print(ba)
# print(bb)

if ab == 'A':
    if aa == 'A':
        print(1)
        # print('www1')
    else: # aa 'B
        if ba == 'A':
            ans = calc(n-3)
            print(ans)
            # print('www2')
        else:
            if bb == 'A':
                ans = pow(2,n-3,MOD)
                print(ans%MOD)
            else:
                ans = pow(2,n-3,MOD)
                print(ans%MOD)
                # else:
                #     ans = calc2(n-3)
                #     print(ans)
                # print('www3')

else:
    if bb == 'B':
        print(1)
        # print('www1')
    else: # aa 'B
        if ba == 'B':
            ans = calc(n-3)
            print(ans)
            # print('www2')
        else:
            if aa == 'B':
                ans = pow(2,n-3,MOD)
                print(ans%MOD)
            else:
                ans = pow(2,n-3,MOD)
                print(ans%MOD)
