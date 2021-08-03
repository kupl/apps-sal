n = int(input())

l = list(map(float, input().split()))

l = sorted([x - int(x) for x in l if x - int(x) != 0])

o = 2 * n - len(l)

su = sum(l)

ans = 0xFFFFFFFFFFFFFFF

for i in range(n + 1):

    if i + o >= n:

        ans = min(ans, abs(i - su))

print("%.3f" % ans)
