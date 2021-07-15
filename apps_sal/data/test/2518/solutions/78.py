n, a, b = list(map(int, input().split()))
dab = a - b
H = []
for _ in range(n):
    H.append(int(input()))
maxh = max(H)

l = 0
r = -(-maxh//b)
def ht(mid):
    cnt = 0
    for h in H:
        rem = h - b*mid
        if rem > 0:
            cnt += -(-rem//dab)
    return cnt <= mid

while (r-l) > 1:
    mid = (l + r) // 2
    if ht(mid):
        r = mid
    else:
        l = mid
print(r)

