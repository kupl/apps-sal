def check(m):
    need = 0
    for (ax, bx) in zip(a, b):
        need += max(0, ax * m - bx)
    return need <= k


(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = 0
r = 10 ** 10
while r - l > 1:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m
print(l)
