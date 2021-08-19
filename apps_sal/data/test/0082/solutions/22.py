(n, k) = map(int, input().split())
a = list(map(int, input().split()))
l = len(a)
s = sum(a)
cur = round(s / l + 1e-07)
count = 0
while cur != k:
    s += k
    l += 1
    cur = round(s / l + 1e-07)
    count += 1
print(count)
