n = int(input().strip())
data = [int(x) for x in input().strip().split(' ')]
t = 0
(mn, mx) = (data[0], data[0])
for x in data:
    mn = min(x, mn)
    mx = max(x, mx)
for x in data:
    if x > mn and x < mx:
        t += 1
print(t)
