n, m, ta, tb, k = list(map(int, input().split()))
fa = list(map(int, input().split()))
fb = list(map(int, input().split()))
arrival = [x + ta for x in fa]
i = 0
j = 0
while(k > 0):
    next = arrival[i]
    fb_time = fb[j]
    while(fb_time < next):
        j += 1
        if j >= m:
            print(-1)
            return
        fb_time = fb[j]
    k -= 1
    i += 1
    if i >= n:
        print(-1)
        return
    j += 1
    if j >= m:
        print(-1)
        return
fb_time = arrival[i]
for k in range(j, m):
    if fb_time <= fb[k]:
        idex = k
        print(fb[k] + tb)
        return
print(-1)
