n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
cap = [0] * (n + 1)
for i in c:
    cap[i - 1] = 1
ans = 0
s = sum(a)
for i in range(len(a) - 1):
    if cap[i] == 1:
        s -= a[i]
        ans += s * a[i]
        #print("s :", s)
        #print("a[i] :", a[i])
    elif cap[i] == 0 and cap[i + 1] == 0:
        #print("a[i] :",a[i])
        #print("a[i+1] :",a[i+1])
        ans += a[i] * a[i + 1]

# print(cap)
if cap[n - 1] == 1:
    s -= a[-1]
    ans += s * a[-1]
    #print("s :",s)
    #print("a[i] :",a[-1])
if cap[0] == 0 and cap[n - 1] == 0:
    ans += a[0] * a[-1]
    print(ans)
else:
    print(ans)
