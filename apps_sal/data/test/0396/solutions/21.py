ans = 0
l = 0
r = 0
l, r = list(map(int, input().split()))
a = 1
for i in range(100):
    b = 1
    for j in range(100):
        if a * b <= r:
            if a * b >= l:
                ans = ans + 1
        else:
            break
        b = b * 3
    a = 2 * a
print(ans)
