T = input().split(' ')
n = int(T[0])
H = int(T[1])
a = 1
b = n
def f(m):
    tot = 42
    if m <= H:
        tot = (m * (m+1)) // 2
    else:
        tot = (H * (H+1)) // 2
        if (m-H) % 2 == 1:
            mx = H + (m - H) // 2
            tot += 2 * ((mx * (mx+1)) // 2 - (H * (H-1)) // 2)
            tot -= H
        else:
            mx = H + (m - H) // 2
            tot += 2 * ((mx * (mx+1)) // 2 - (H * (H-1)) // 2)
            tot -= H
            tot -= mx
    return tot >= n
if n==1:
    print(1)
else:
    m = (a+b)//2
    while b-a > 1:
        if f(m):
            b = m
        else:
            a = m
        m = (a+b)//2
    print(b)

