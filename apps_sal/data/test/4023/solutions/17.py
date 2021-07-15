n = int(input())
a = list(map(int, input().split()))
k = max(a)
f = -1
q = (10 ** 6) * [-1]
pnt = -1
ans = "YES"
for i in range(n):
    if pnt == -1:
        pnt += 1
        q[pnt] = a[i]
        f = i
    else :
        if q[pnt] == a[i]:
            q[pnt] = -1
            pnt -= 1
        elif q[pnt] < a[i]:
            ans = "NO"
        else:
            pnt += 1
            q[pnt] = a[i]
            f = i
if pnt == 0:
    if q[0] != k:
        ans = "NO"
if pnt > 0 or(f == n -1 and a[-1] != k):
    ans = "NO"
print(ans)

