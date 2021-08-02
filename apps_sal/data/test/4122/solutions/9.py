import math
h, n = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
mn = 0
sm = 0
counter = 0
done = False
for i in l:
    counter += 1
    sm += i
    mn = min(mn, sm)
    if h + mn <= 0 and done == False:
        print(counter)
        done = True
if sm >= 0:
    if done == False:
        print(-1)
else:
    nh = h + mn
    it = nh // -sm
    if nh % -sm:
        it += 1
    ans = it * n
    h = h + it * sm
    for i in range(n):
        h = h + l[i]
        ans += 1
        if h <= 0 and done == False:
            print(ans)
            break
