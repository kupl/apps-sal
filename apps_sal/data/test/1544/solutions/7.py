def C(frm, what):
    ans = 1
    for i in range(what):
        ans *= frm - i
        ans = ans // (i + 1)
    return ans

n = int(input())
print (C(4 + n, n - 1) * C(2 + n, n - 1))
