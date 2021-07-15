K, N = map(int, input().split())
Alst = list(map(int, input().split()))
zero = Alst[0] + K
M = 0
now = Alst[0]
for i in Alst:
    dis = i - now
    if dis > M:
        M = dis
    now = i

last = zero - now
if last > M:
    M = last

print(K - M)
