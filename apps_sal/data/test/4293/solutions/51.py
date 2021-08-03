

P, Q, R = list(map(int, input().split()))


abc = P + Q
acb = Q + R
bca = P + R
print((min(abc, acb, bca)))
