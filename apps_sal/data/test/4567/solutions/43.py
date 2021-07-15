n = int(input())
a = [int(input()) for i in range(n)]
a.sort()

ans = sum(a)
if ans % 10 != 0:
    print(ans)
    return
    
flg = False
for i in range(n):
    if a[i] % 10 != 0:
        ans -= a[i]
        flg = True
        break
print(ans) if flg else print(0)
