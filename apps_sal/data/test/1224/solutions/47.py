N = int(input())

maxa = 39
maxb = 27
det = False
for a in range(1, 39):
    for b in range(1, 27):
        if 3**a + 5**b == N:
            ans1, ans2 = a, b
            det = True
if det:
    print("{} {}".format(ans1, ans2))
else:
    print(-1)
