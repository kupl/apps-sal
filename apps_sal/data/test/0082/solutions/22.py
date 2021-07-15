n, k = map(int, input().split())
a = list(map(int, input().split()))
l = len(a)
s = sum(a)
cur = round(s / l + 0.0000001)
count = 0
while cur != k:
    s += k
    l += 1
    cur = round(s / l + 0.0000001)
    count += 1
print(count)
