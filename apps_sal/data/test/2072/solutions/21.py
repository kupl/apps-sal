n = int(input())
x = list(map(float, input().split()))
v = list(map(float, input().split()))

def func(Tx):
    nonlocal x
    nonlocal v
    nonlocal n

    times = 0
    for j in range(n):
        times = max(abs(Tx-x[j])/v[j],times)
    return times


l = min(x); r = max(x)
ans = float(0)

for i in range(70):
    m1 = (2*l + r)/3
    m2 = (2*r + l)/3
    if(func(m1) < func(m2)):
        r = m2
    else:
        l = m1

ans = func((m1+m2)/2)
print(ans)

