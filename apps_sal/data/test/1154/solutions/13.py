n, h, k = map(int, input().split())
hei = list(map(int, input().split()))
sec = 0
cur = 0
i = 0
while i < len(hei):
    sec += cur // k
    cur = cur % k
    if i < len(hei) and cur + hei[i] > h:
        sec += cur // k + 1
        cur = 0
        cur += hei[i]
        i += 1
    while i < len(hei) and cur + hei[i] <= h:
        cur += hei[i]
        i += 1
sec += cur // k
cur = cur % k
if cur != 0:
    sec += 1
print(sec)
