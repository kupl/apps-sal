n, k = map(int, input().split())
d = list(map(int, input().split()))
p = []
count = 0
count1 = 0
for i in range(len(d)):
    if d[i] >= 0:
        count += 1
    if d[i] < 0 or i == len(d) - 1:
        p.append(count)
        count = 0
        count1 += 1
if d[len(d) - 1] >= 0:
    count1 -= 1
if count1 == 0:
    print(0)
    return
a = p.pop() if d[len(d) - 1] >= 0 else 0
if len(p) > 0:
    p.reverse()
    p.pop()
    p.sort()
count = k - len(p) - 1 if count1 > 1 else k - count1
if count < 0:
    print(-1)
    return
count1 = 0
for i in range(len(p)):
    if(count - p[i] >= 0):
        count1 += 1
        count -= p[i]
    else:
        break
ans = 2 * (len(p) + 1 - count1)
if count - a >= 0:
    ans -= 1
print(ans)
