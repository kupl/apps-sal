x = input()
n = len(x)
if n == 1:
    print(x)
    return
ans = ""
s = 0
ps = 0
pn = ""
for i in range(n):
    ts = ps + int(x[i]) - 1 + 9 * (n - i - 1)
    if ts >= s:
        ans = pn + str(int(x[i]) - 1) + "9" * (n - i - 1)
        s = ts
    ps += int(x[i])
    pn += x[i]
if ps >= s:
    ans = pn
print(int(ans))
