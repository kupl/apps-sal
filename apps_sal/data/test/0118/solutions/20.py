t, s, x = list(map(int, input().split()))
r = (x - t) % s
if (r == 0  and x >= t) or (r == 1 and x > t + 1):
    print("YES")
else:
    print("NO")

