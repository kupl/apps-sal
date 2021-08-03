import sys
n = int(input())
a = [0] + list(map(int, input().split()))
dp = {}
dp1 = {}
for i in range(int(input())):
    l, r = list(map(int, sys.stdin.readline().split()))
    ans = 0

    def check(l, r):
        nonlocal ans
        # print(ans)
        if (l, r) in dp:
            return dp[(l, r)]
        else:
            if (l == r):
                dp[(l, r)] = (a[l], 0)
                return dp[(l, r)]
            else:
                mid = (l + r) // 2
                p1 = check(l, mid)
                p2 = check(mid + 1, r)
                # p=check(l,mid)[0] + check(mid+1,r)[0]
                if p1[0] + p2[0] >= 10:
                    dp[(l, r)] = ((p1[0] + p2[0]) % 10, p1[1] + p2[1] + 1)
                else:
                    dp[(l, r)] = ((p1[0] + p2[0]) % 10, p1[1] + p2[1])
                # print(p,ans)
                return dp[(l, r)]
    print(check(l, r)[1])
    # print()
