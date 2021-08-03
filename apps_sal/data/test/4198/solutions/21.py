def LI():
    return list(map(int, input().split()))


A, B, X = LI()
ans = 0
for i in range(1, 10):
    x = (X - B * i) // A
    L = len(str(x))
    xmin = int("1" + "0" * (i - 1))
    xminm = xmin * A + B * i
    xmax = int("9" * i)
    xmaxm = xmax * A + B * i
    if xminm > X:
        continue
    elif xmaxm <= X:
        ans = xmax
    elif x <= X:
        ans = x
x = 1000000000 * A + B * 10
if x <= X:
    ans = 1000000000
print(ans)
