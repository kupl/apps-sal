n = int(input())
a = list(map(int, input().split()))
ma = 0
last = 0
cur = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        cur += 1
    else:
        ma = max(ma, min(last, cur))
        last = cur
        cur = 1
    ma = max(ma, min(last, cur))
print(2 * ma)
