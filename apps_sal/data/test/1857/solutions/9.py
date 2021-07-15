def C(frm, what):
    ans = 1
    for i in range(what):
        ans *= frm - i
        ans = ans // (i + 1)
    return ans
 
n = int(input())
ans = C(n, 5) * C(n, 5) * 120
print (ans)
