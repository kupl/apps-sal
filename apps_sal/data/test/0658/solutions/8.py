(n, w, v, u) = list(map(int, input().split()))
(x, y) = list(map(int, input().split()))
razn = ozhid = v * y - x * u
for i in range(1, n):
    (x, y) = list(map(int, input().split()))
    r = v * y - x * u
    if r > razn:
        razn = r
    if r < ozhid:
        ozhid = r
if ozhid >= 0 or razn <= 0:
    print(w / u)
else:
    print(w / u - ozhid / (u * v))
