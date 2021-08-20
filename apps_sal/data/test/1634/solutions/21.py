(c1, c2, c3, c4) = map(int, input().split())
(n, m) = map(int, input().split())
bus = list(map(int, input().split()))
p = c2 // c1
for idx in range(n):
    if bus[idx] > 0:
        if bus[idx] > p:
            bus[idx] = c2
        else:
            bus[idx] = bus[idx] * c1
b_total = min(sum(bus), c3)
trol = list(map(int, input().split()))
for idx in range(m):
    if trol[idx] > 0:
        if trol[idx] > p:
            trol[idx] = c2
        else:
            trol[idx] = trol[idx] * c1
t_total = min(sum(trol), c3)
print(min(b_total + t_total, c4))
