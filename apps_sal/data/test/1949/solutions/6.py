(n, k) = map(int, input().split())
l = sorted(list(map(int, input().split())))
(a, m) = (0, 0)
for i in l:
    if i == a:
        continue
    if m == k:
        break
    print(i - a)
    a = i
    m += 1
while m < k:
    print(0)
    m += 1
