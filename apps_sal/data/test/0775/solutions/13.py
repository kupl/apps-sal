(n, m, k) = list(map(int, input().split()))
hole = set(map(int, input().split()))
fall = 0
current = 1
for i in range(k):
    if fall == 0 and current in hole:
        fall = current
    (u, v) = list(map(int, input().split()))
    if u == current:
        current = v
    elif v == current:
        current = u
if fall != 0:
    print(fall)
else:
    print(current)
