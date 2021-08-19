(q, w) = list(map(int, input().split()))
a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = 1
t = a[q] - (8 - w)
while t > 0:
    ans += 1
    t -= 7
print(ans)
