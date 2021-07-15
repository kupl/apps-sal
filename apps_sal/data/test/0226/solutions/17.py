
def dp(a, i,control):
    if i >= len(a):
        return 0;
    if dp_list[control][i] != -1:
        return dp_list[control][i]
    else:
        if control:
            res = max(a[i] + dp(a, i+1, False), dp(a , i+1 , True))
        else:
            res = min(dp(a, i+1, True), a[i] + dp(a , i+1 , False))
        dp_list[control][i] = res
        return dp_list[control][i]

n = int(input())
dp_list = [list(-1 for i in range(n)) , list(-1 for i in range(n)) ]
a = list(map(int, input().split(" ")))
res = dp(a , 0, True)
print("%s %s" %(sum(a) - res , res ))
