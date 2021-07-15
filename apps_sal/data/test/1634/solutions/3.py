c1, c2, c3, c4 = map(int, input().split())
n, m = map(int, input().split())
bus = list(map(int, input().split()))
trol = list(map(int, input().split()))

mbus = [0] * n
mtrol = [0] * m

for i in range (n):
    mbus[i] = min(bus[i] * c1, c2)
sbus = min(sum(mbus), c3)

for i in range (m):
    mtrol[i] = min(trol[i] * c1, c2)
strol = min(sum(mtrol), c3)

res = min(sbus + strol, c4)

print(res)
