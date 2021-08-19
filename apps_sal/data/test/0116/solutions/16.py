temp = input().split()
l1 = int(temp[0])
r1 = int(temp[1])
l2 = int(temp[2])
r2 = int(temp[3])
k = int(temp[4])
t = 0
l = max(l1, l2)
r = min(r1, r2)
if r >= l:
    t += r - l + 1
if l <= k and k <= r:
    t -= 1
print(t)
