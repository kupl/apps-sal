I = lambda : map(int, input().split())
n, a = I()

exp = 999999999999
ans = 0

for i in range(1, n-1):
    newexp = abs((i*180.0)/(n*1.0) - a)
    if newexp < exp:
        ans = i
        exp = newexp

print(2, 1, 2+ans)
