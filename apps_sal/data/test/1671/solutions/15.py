n = int(input())
m = list(map(int, input().split()))
ss = sum(m)
dd = ss // n
maxdd = ss % n
mindd = n - maxdd
ans = 0
for a in m:
    if a >= dd and maxdd == 0:
        ans += a - dd
        mindd -= 1
    elif a > dd:
        if maxdd > 0:
            ans += a - (dd + 1)
            maxdd -= 1
        else:
            ans + + a - dd
            mindd -= 1
print(ans)
