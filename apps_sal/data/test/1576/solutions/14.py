a = input()
ans = ""
if (len(a)%2 == 0):
    i = 0
    while i < len(a)/2:
        ans+=a[-i-1]+a[i]
        i+=1
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end="")
else:
    i = 0
    while i < len(a) / 2:
        ans += a[i] + a[-i-1]
        i += 1
    for i in range(len(ans) - 2, -1, -1):
        print(ans[i], end="")
