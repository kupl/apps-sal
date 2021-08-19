n = int(input())
mt = 0
mq = 0
t = 0
q = 0
for i in range(n):
    (ti, ci) = list(map(int, input().split()))
    q = max(0, q - ti + t)
    t = ti
    q += ci
    mq = max(mq, q)
    mt = t + q
print(mt, mq)
