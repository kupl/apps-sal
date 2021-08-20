t = [int(x) for x in input().split()]
t.sort()
ans = t[2] - t[1] - t[0] + 1
if ans < 0:
    ans = 0
print(ans)
