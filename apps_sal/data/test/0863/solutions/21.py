def meet(a, b):
    return max(a[0], b[0]) < min(a[1], b[1])


(a, ta) = list(map(int, input().split()))
(b, tb) = list(map(int, input().split()))
(h, m) = list(map(int, input().split(':')))
ts = (h - 5) * 60 + m
ts = (ts, ts + ta)
cnt = 0
i = 0
while i * b <= (23 - 5) * 60 + 59:
    if meet((i * b, i * b + tb), ts):
        cnt += 1
    i += 1
print(cnt)
