from collections import defaultdict
n, s = int(input()), []
for i in range(n):
    a = [int(x) for x in input().split()]
    s += [(a[0], 0), (a[1], 1)]
s.sort()
now = 0
rev = defaultdict(int)
for a, b in zip(s, s[1:]):
    # print(a,b)
    if(a[1] == 0):
        now += 1
        # print("now: %d" % now)
        rev[now] += b[0] - a[0]
        if b[1] == 1:
            # print("add %d" % (b[0] - a[0] + 1))
            rev[now] += 1
        # else:
        #   print("add %d" % (b[0] - a[0]))
    else:
        now -= 1
        # print("now: %d" % now)
        if b[0] != a[0]:
            rev[now] += b[0] - a[0]
            if b[1] == 0:
                # print("add %d" % (b[0] - a[0] - 1))
                rev[now] -= 1
            # else:
            #   print("add %d" % (b[0] - a[0]))
# print(rev)
for i in range(1, n + 1):
    print(rev[i], end=" ")
